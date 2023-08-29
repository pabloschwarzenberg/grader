import random
def ocultar_letras(palabra, cantidad):
	contador=0
	cantidad=int(cantidad)
	x=str(palabra)

	while True:
		letra_i=str(x[random.randint(0,len(x)-1)])
		x=x.replace(letra_i,"-",1)
		if x.count("-")==cantidad:
			break
	return x

def revisar_letra(palabra_secreta,palabra,letra):
	x=palabra
	if letra in palabra_secreta:
		lista=[]
		for i in range(len(palabra_secreta)-1):
			if palabra_secreta[i]==letra:
				lista.append(i)
	for i in lista:    #puras ubicaciones
		x=x.replace(x[i],letra,1)
	return x