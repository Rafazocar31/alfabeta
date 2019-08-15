import sys

def importarArchivosDeAlfabeta(ruta_manual, ruta_manextra):
	archivo_dat = open(ruta_manual, encoding="ansi")
	archivo_extra = open(ruta_manextra)

	lineas_dat = archivo_dat.readlines()

	for line in lineas_dat:
		line = line.strip()

		troquel = line[:7]
		nombre = line[7:51].strip()
		presentacion = line[51:75].strip()
		Laboratorio = line[85:101].strip()
		precio = line[105:110].strip()
		precio = float(precio) / 100
		fechavc = line[110:118].strip()
		importado = line[119:120].strip()
		tipoventa = line[120:121].strip()

	
		
		print(f'El troquel es: "{troquel}"')
		print(f'El nombre es: "{nombre}"')
		print(f'La presentación es: "{presentacion}"')
		print(f'El Laboratorio es: "{Laboratorio}"')
		print(f'El precio es: "{precio}"')
		print(f'La fecha vigente de precio es: "{fechavc}"')
		print(f'La importacion es:"{importado}"')
		print(f'El tipo de venta es:"{tipoventa}"')


		sys.exit()

def app():
	archivos_alfabeta = importarArchivosDeAlfabeta("archivos_alfabeta/manual.dat", "archivos_alfabeta/manextra.txt")
	
app()