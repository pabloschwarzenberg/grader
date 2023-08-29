def rot13(palabra):
	abc="abcdefghijklmnopqrstuvwxyz"
	cba="nopqrstuvwxyzabcdefghijklm"
	string=""
	for letra in palabra:
		posicion=abc.find(letra)
		letra=letra.replace(letra, cba[posicion])
		string+=letra

	return string
      

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           