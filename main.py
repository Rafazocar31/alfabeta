import sys
import datetime
import csv

def importarDrogasDeAlfabeta(ruta_manual, ruta_manextra):
	drogas = {}

	archivo_dat = open(ruta_manual, encoding='ansi')
	archivo_extra = open(ruta_manextra, encoding='ansi')

	lineas_dat = archivo_dat.readlines()
	lineas_extra = archivo_extra.readlines()

	#procesamos manual.dat
	for linea in lineas_dat:
		linea = linea.strip()

		fecha_de_vigencia = linea[110:118].strip()
		fecha_de_vigencia = datetime.datetime.strptime(fecha_de_vigencia, '%Y%m%d')
		fecha_de_vigencia = fecha_de_vigencia.strftime('%d/%m/%Y')

		precio = linea[105:110].strip()
		precio = float(precio) / 100

		regmed = int(linea[126:131].strip())

		drogas[regmed] = {}

		drogas[regmed]['troquel'] = linea[:7].strip()
		drogas[regmed]['nombre'] = linea[7:51].strip()
		drogas[regmed]['presentacion'] = linea[51:75].strip()
		drogas[regmed]['laboratorio'] = linea[85:101].strip()
		drogas[regmed]['precio'] = precio
		drogas[regmed]['fecha_de_vigencia'] = fecha_de_vigencia
		drogas[regmed]['importado'] = linea[119:120].strip()
		drogas[regmed]['tipoventa'] = linea[120:121].strip()
		drogas[regmed]['iva'] = linea[122:123].strip()
		drogas[regmed]['cod_laboratorio'] = linea[123:126].strip()
		drogas[regmed]['codigo_de_barras'] = linea[132:145].strip()
		drogas[regmed]['unidades'] = linea[147:149].strip()
	
	# procesamos manextra.txt
	for linea in lineas_extra:
		linea = linea.strip()

		regmed = int(linea[:5])

		drogas[regmed]['cod_accion_farmacologica'] = linea[9:12].strip()
		drogas[regmed]['cod_monodroga'] = linea[12:16].strip()
		drogas[regmed]['cod_formas'] = linea[20:22].strip()
		drogas[regmed]['potencia'] = linea[22:38].strip()
		drogas[regmed]['cod_unidad_potencia'] = linea[38:43].strip()
		drogas[regmed]['cod_tipo_unidad'] = linea[43:48].strip()
		drogas[regmed]['cod_via'] = linea[48:53].strip()
	
	return drogas

def grabarDrogasDeAlfabetaAArchivo(drogas, ruta_output):
	archivo_output = open(ruta_output, 'w', encoding='ansi', newline='')

	columnas_csv = ['troquel', 'nombre', 'presentacion', 'laboratorio', 'precio', 'fecha_de_vigencia', 'importado', 'tipoventa', 'iva', 'cod_laboratorio', 'codigo_de_barras', 'unidades', 'cod_accion_farmacologica', 'cod_monodroga', 'cod_formas', 'potencia', 'cod_unidad_potencia', 'cod_tipo_unidad', 'cod_via']

	grabador_de_csv = csv.DictWriter(archivo_output, fieldnames=columnas_csv, delimiter=';')
	grabador_de_csv.writeheader()
	for droga in drogas:
		grabador_de_csv.writerow(drogas[droga])

def app():
	drogas = importarDrogasDeAlfabeta('archivos_alfabeta/manual.dat', 'archivos_alfabeta/manextra.txt')
	grabarDrogasDeAlfabetaAArchivo(drogas, 'output.csv')
	
app()
