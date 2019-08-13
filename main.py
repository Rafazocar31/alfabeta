import sys

archivo_dat = open("archivos_alfabeta/manual.dat", "r", encoding="ansi")
archivo_extra = open("archivos_alfabeta/manextra.txt", "r")

contenido_dat = archivo_dat.readlines()


for line in contenido_dat:
	line = line.strip()

	troquel = line[:7]
	nombre = line[7:44].strip()
	presentacion = line[44:68].strip()
	
	print(troquel)
	print(nombre)
	print(presentacion)

	sys.exit()