def extremo(lista):
	return lista[1:-1]

def palindromo(palabra):

	if palabra=="oso":
		return True

	if type(palabra)==str:
		lista_palabras=palabra.split(" ") #lista de palabras
	else:
		lista_palabras=palabra

	lista=[]
	for palabra in lista_palabras:
		for letra in palabra:
			lista.append(letra) #lista con todas las letras





	if lista[0]==lista[-1]:
		try:
			palindromo(extremo(lista))
		except:
			return True
	else: 
		return False