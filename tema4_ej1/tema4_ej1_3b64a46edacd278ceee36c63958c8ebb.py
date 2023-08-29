import random

palabras = ["Barco","Camaron","Tartaro","Muerte","lepidoptero"]

def ocultar_letras(palabra,cantidad):
	LPalabra = list(palabra)
	cont = 0
	for i in LPalabra:
		if (cont < cantidad):
			n = random.randint(0,len(palabra)-1)
			if (LPalabra[n] != "_"):
				LPalabra.insert(n,"_")
				LPalabra.pop(n+1)
				cont += 1
	palabra = "".join(LPalabra)
	return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
	listaS = []
	lista = []
	listaL = []
	for i in range(len(palabra)):
		listaS.append(palabra_secreta[i])
		lista.append(palabra[i])
	if (len(letra) == 1):
		for i in range(len(palabra)):
			if (listaS[i] != lista[i] and listaS[i] == letra):
				lista.insert(i+1,letra)
				lista.pop(i)
		return ("".join(lista))
	elif(len(letra) == len(palabra)):
		for i in letra:
			listaL.append(i)
		for i in range(len(palabra)):
			if (listaS[i] != lista[i] and listaS[i] == listaL[i]):
				lista.insert(i+1,letra[i])
				lista.pop(i)
		return ("".join(lista))
	else:
		return (palabra)
		
	
def Elejir_palabra(palabras):
	return(palabras[random.randint(0,len(palabras)-1)])

palabraJuego = Elejir_palabra(palabras).lower()
palabraEscondida = ocultar_letras(palabraJuego,random.randint(0,len(palabraJuego)-1)).lower()
i =0
a = ""
if __name__ == "__main__":
	a = input("")

  
while(i < 7):
	print(palabraEscondida)
	palabraEscondida = revisar_letra(palabraJuego,palabraEscondida,a.lower())
	i += 1


         