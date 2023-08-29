def rot13(palabra):
    abecedario="abcdefghijklmnopqrstuvwxyz"
    palabra1=""
    for x in palabra:
        palabra1 += abecedario[(abecedario.find(x)+13)%26]
    return palabra1
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           