hombre_imaginario="""
El hombre imaginario
vive en una mansion imaginaria
rodeada de arboles imaginarios
a la orilla de un rio imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcon imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):

	texto=frase.split()
	textop=len(frase)
	n_texto=len(texto)
	num_texto=(len(texto))
	
	caracteres=(sum(len(palabra) for palabra in texto))-(frase.count("."))
	
	num_caracteres=(sum(len(textop) for textop in frase))
	
	largo_promedio=(caracteres / n_texto)
	
	num_espacios=(frase.count(" "))
	caracteres_puntuacion=frase.count('.')

	return num_texto, num_caracteres, largo_promedio, num_espacios, caracteres_puntuacion

if __name__=='__main__':
	
	print(estadisticas_frase(hombre_imaginario))