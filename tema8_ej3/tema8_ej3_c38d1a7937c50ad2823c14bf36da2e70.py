hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
	caracteres = len(frase) #Cuenta total caracteres
	char_punt = frase.count('.') #Cuenta caracteres de puntuacion
	reemplazo = str.maketrans('.', ' ')
	frase = str.translate(frase, reemplazo)
	frase = frase.strip()
	prom = 0
	cantpal = 0
	listpal = frase.split()
	for i in listpal: #Cuenta cantidad de palabras
		if listpal != '.':
			cantpal += 1
	cantspace = frase.count(' ') #Cuenta cantidad de espacios
	for j in listpal: #Obtiene el promedio del largo de las palabras
		prom += len(j)
		print(prom)
	prom = prom/cantpal

	return cantpal, caracteres, prom, cantspace, char_punt

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         