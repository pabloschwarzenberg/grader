string = """
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

def estadisticas_frase(string):
	string.lower
	espacios=0
	caracteres=0
	for i in string:
		caracteres+=1
		if i == " ":
			espacios+=1
	
	palabras=string.split("\n")
	palabras_solas=[]
	for palabra in palabras:
		if " " in palabra==False:
			palabras_solas.append(palabra)
		else:
			separada=palabra.split(" ")
			for i in separada:
				palabras_solas.append(i)
	palabras=palabras_solas
	for i in palabras:
		if i =="":
			palabras.remove("")

	caracteres_especiales=[".", ","]
	numero_palabras=0
	numero_letras=0
	numero_caracteres_especiales=0
	for palabra in palabras:
		numero_palabras+=1
		for letra in palabra:
			if letra =="." :
				numero_caracteres_especiales+=1
			else:
				numero_letras+=1

		
	print(palabras)
	largo_promedio= numero_letras/numero_palabras
	return numero_palabras, caracteres, largo_promedio, espacios, numero_caracteres_especiales


    
         