def buscarTodas(a,b):
	lista = []
	lista2 = []
	retorno = ""
	for i in range(len(a)):
		if (a[i].upper() == b.upper()):
			lista.append(str(i))
			lista.append(" ")
	lista2 = lista[::-1]
	lista2.remove(" ")
	lista = lista2[::-1]
	for i in lista:
		retorno += i
	return(retorno)

if __name__ == "__main__":
    pass
           