import sys

archivo_dat = open("archivos_alfabeta/manual.dat", "r", encoding="ansi")
archivo_extra = open("archivos_alfabeta/manextra.txt", "r")

lineas_dat = archivo_dat.readlines()


for line in lineas_dat:
	line = line.strip()

	troquel = line[:7]
	nombre = line[7:51].strip()
	presentacion = line[51:75].strip()
	
	print(f'El troquel es: "{troquel}"')
	print(f'El nombre es: "{nombre}"')
	print(f'La presentación es: "{presentacion}"')

	sys.exit()