#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
	palabra1 = palabra1
	palabra2 = palabra2
	lista1 = []
	lista2 = []
	for i in palabra1:
		lista1.append(i)
	for i in palabra2:
		lista2.append(i)
	if (palabra1 >= palabra2):
		masGrande = len(palabra1)
	elif(palabra2 >= palabra1):
		masGrande = len(palabra2)
#	for i in range(masGrande-1):
	for j in palabra2:
		if (j in lista1):
			lista1.remove(j)
	for k in palabra1:
		if (k in lista2):
			lista2.remove(k)
				
	print(lista1)
	print(lista2)
	if(len(lista1) == 1 and len(lista2) == 1):
		return("1S")
	if(len(lista1) == 1 or len(lista2) == 1):
		return("IB")
	if(len(lista1) == 0 and len(lista2) == 0):
		return("0D")
	if(len(lista1) > 1 or len(lista2) > 1):
		return("+1")

if __name__=="__main__":
    pass
           