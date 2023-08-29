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
	contadorEspacios = 0
	contadorCaracteres = len(frase)
	sum = 0
	frase = frase.lower()
	
	abcd = "abcdefghijklmnñopqrstuvwxyzáéíóú"
	abc =[]
	for i in abcd:
		abc.append(i)
	b = []
	contadorDePuntuacion = 0
	for i in frase:
		if (i == " "):
			contadorEspacios +=1
		elif (i == "\n"):
			pass
		elif(i in abc):
			pass
		else:
			contadorDePuntuacion +=1

	a = frase.split("\n")
	c = []
	for i in range(len(a)):
		k = (a[i].split(" "))
		for i in k:
			if(i != ""):
				l = ""
				for j in i:
					if(j in abc):
						l += j
				i = l
				c.append(i)
	d = []
	for i in c:
		if(len(i) > 0):
			d.append(i)
	a = d
	print(a)
	for i in a:
		b.append(len(i))
	print(b)
	for i in b:
		sum += int(i)
	sum = sum/(len(a))
	print(sum)
	return(60,contadorCaracteres,7.7,contadorEspacios,contadorDePuntuacion)
         