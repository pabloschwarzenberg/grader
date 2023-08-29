#ROT13

def rot13(palabra):
	desplazamiento = 13
	cifrado = ""
	if palabra == palabra.upper():
		lista = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
	else:
		lista = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
	for i in palabra:
		if i in lista:
			cifrado += lista[(lista.index(i)+desplazamiento%(len(lista)))]
		else:
			cifrado += i
	return cifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           

           