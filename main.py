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
		
		print(f'El troquel es: "{troquel}"')
		print(f'El nombre es: "{nombre}"')
		print(f'La presentación es: "{presentacion}"')
		print(f'El Laboratorio es: "{Laboratorio}"')
		print(f'El precio es: "{precio}"')

		sys.exit()

def app():
	archivos_alfabeta = importarArchivosDeAlfabeta("archivos_alfabeta/manual.dat", "archivos_alfabeta/manextra.txt")
	
app()