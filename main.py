import sys
import datetime
import csv
import sqlite3



def importarDrogasDeAlfabeta(ruta_manual, ruta_manextra):
	drogas = {}

	archivo_dat = open(ruta_manual, encoding='ansi')
	archivo_extra = open(ruta_manextra, encoding='ansi')

	lineas_dat = archivo_dat.readlines()
	lineas_extra = archivo_extra.readlines()

	#procesamos manual.dat
	for linea in lineas_dat:
		linea = linea.strip()

		regmed = int(linea[126:131])

		fecha_de_vigencia = linea[110:118].strip()
		fecha_de_vigencia = datetime.datetime.strptime(fecha_de_vigencia, '%Y%m%d')
		fecha_de_vigencia = fecha_de_vigencia.strftime('%d/%m/%Y')

		precio = float(linea[105:110]) / 100

		drogas[regmed] = {}

		drogas[regmed]['troquel'] = linea[:7].strip()
		drogas[regmed]['nombre'] = linea[7:51].strip()
		drogas[regmed]['presentacion'] = linea[51:75].strip()
		drogas[regmed]['laboratorio'] = linea[85:101].strip()
		drogas[regmed]['precio'] = precio
		drogas[regmed]['fecha_de_vigencia'] = fecha_de_vigencia
		drogas[regmed]['importado'] = int(linea[119:120])
		drogas[regmed]['tipoventa'] = int(linea[120:121])
		drogas[regmed]['iva'] = linea[122:123].strip()
		drogas[regmed]['cod_laboratorio'] = int(linea[123:126])
		drogas[regmed]['codigo_de_barras'] = linea[132:145].strip()
		drogas[regmed]['unidades'] = linea[147:149].strip()
	
	# procesamos manextra.txt
	for linea in lineas_extra:
		linea = linea.strip()

		regmed = int(linea[:5])

		drogas[regmed]['cod_accion_farmacologica'] = int(linea[9:12])
		drogas[regmed]['cod_monodroga'] = int(linea[12:16])
		drogas[regmed]['cod_formas'] = int(linea[20:22])
		drogas[regmed]['potencia'] = linea[22:38].strip()
		drogas[regmed]['cod_unidad_potencia'] = int(linea[38:43])
		drogas[regmed]['cod_tipo_unidad'] = int(linea[43:48])
		drogas[regmed]['cod_via'] = int(linea[48:53])
	
	return drogas

def grabarDrogasDeAlfabetaEnArchivoCSV(drogas, ruta_output):
	archivo_output = open(ruta_output, 'w', encoding='ansi', newline='')

	columnas_csv = ['troquel', 'nombre', 'presentacion', 'laboratorio', 'precio', 'fecha_de_vigencia', 'importado', 'tipoventa', 'iva', 'cod_laboratorio', 'codigo_de_barras', 'unidades', 'cod_accion_farmacologica', 'cod_monodroga', 'cod_formas', 'potencia', 'cod_unidad_potencia', 'cod_tipo_unidad', 'cod_via']

	grabador_de_csv = csv.DictWriter(archivo_output, fieldnames=columnas_csv, delimiter=';')
	grabador_de_csv.writeheader()
	for droga in drogas:
		grabador_de_csv.writerow(drogas[droga])

def AbrirBaseDeDatosSQLite(ruta_output):
	conn = sqlite3.connect(ruta_output)
	return conn

def crearTablaDrogas(conn):
	cursor = conn.cursor()

	cursor.execute('DROP TABLE IF EXISTS drogas')
	conn.commit()

	cursor.execute("""
		CREATE TABLE IF NOT EXISTS drogas(
			troquel STRING(8),
			nombre STRING(64),
			presentacion STRING(64),
			laboratorio STRING(64),
			precio FLOAT,
			fecha_de_vigencia DATE,
			importado TINYINT,
			tipoventa TINYINT,
			iva STRING(8),
			cod_laboratorio INT,
			codigo_de_barras STRING(16),
			unidades INT,
			cod_accion_farmacologica INT,
			cod_monodroga INT,
			cod_formas INT,
			potencia STRING(16),
			cod_unidad_potencia INT,
			cod_tipo_unidad INT,
			cod_via INT
		);
	""")
	conn.commit()

def GrabarDrogasEnSQLite(conn, drogas):
	cursor = conn.cursor()

	for droga in drogas:
		droga = drogas[droga]

		columnas = ', '.join(droga.keys())
		eses = ', '.join(['?'] * len(droga))
		query = f'INSERT INTO drogas ( {columnas} ) VALUES ( {eses} );'

		cursor.execute(query, list(droga.values()))
	
	conn.commit()

def main():
	drogas = importarDrogasDeAlfabeta('archivos_alfabeta/manual.dat', 'archivos_alfabeta/manextra.txt')
	# grabarDrogasDeAlfabetaEnArchivoCSV(drogas, 'output.csv')
	conn = AbrirBaseDeDatosSQLite('alfabeta.sqlite3')
	crearTablaDrogas(conn)
	GrabarDrogasEnSQLite(conn, drogas)

main()
