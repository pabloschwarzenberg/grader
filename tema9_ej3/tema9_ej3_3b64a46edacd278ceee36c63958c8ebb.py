def decodificar(mensaje):
	traduccion = ""
	traduccionFinal = ""
	tranf = [128,64,32,16,8,4,2,1]
	list = []
	suma = 0
	cont = 0
	for i in mensaje:
		if(i != ","):
			suma += int(i) * tranf[cont]
			cont += 1
		elif(i == ","):
			list.append(str(suma))
			suma = 0
			list.append(i)
		if (cont == 8):
			cont = 0
	list.append(str(suma))
	suma = 0
	print(list)
	for i in list:
		if(i != ","):
			traduccion += i			
		else:
			traduccionFinal += str(chr(int(traduccion)))
			traduccion = ""
	traduccionFinal += str(chr(int(traduccion)))
	traduccion = ""
	return traduccionFinal

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         