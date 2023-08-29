def rot13(texto):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    encripto = ""
    for i in texto:
        if i in alfabeto:
            indice = alfabeto.index(i)
            nuevaposi = (indice + 13) % len(alfabeto)
            encripto += alfabeto[nuevaposi]
    return encripto


if __name__=="__main__":
    texto=input("Ingresa la palabra que quieras encriptar: ")
    texto.lower()
    resultado=rot13(texto)
    print("El resultado es: ",resultado)
           