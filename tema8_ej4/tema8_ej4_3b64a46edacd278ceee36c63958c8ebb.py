def rot13(palabra):
	palabra = palabra.upper()
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	abc13 = []
	retorno = ""
	a = 0
	c = 13
	for i in palabra:
		if (i != " "):
			if (abc.index(i) + c > len(abc)-1):
				a = abc.index(i) - len(abc) + c 
				print(a)
			else:
				a = abc.index(i) + c
				print(a)
			abc13.append(abc[a])
		elif(i == " "):
			abc13.append(" ")
	for i in abc13:
		retorno += i
	return (retorno.lower())

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           