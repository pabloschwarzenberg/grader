def rot13(palabra):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    texto = ""
    for letter in palabra:
        pos = alpha.find(letter)
        if pos != -1:
            texto+= alpha[(pos+13)%26]
        else:
            texto+=""
    return texto

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           