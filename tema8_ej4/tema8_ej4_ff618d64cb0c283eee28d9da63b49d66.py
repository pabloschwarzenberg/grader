def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

def rot13(palabra):
	abc = "abcdefghijklmnopqrstuvwxyz"
	abc_multiplicado = abc*3
	resultado = ""
	for char in palabra:
		indice = abc_multiplicado.index(char)
		resultado += abc_multiplicado[indice+13]
	return resultado

if __name__ == "__main__":
	palabra = input("Ingrese la palabra que desee encriptar: ")
	palabra.lower()
	resultado = rot13(palabra)
	print("El resultado es: " + resultado)
