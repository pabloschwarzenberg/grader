def rot13(palabra):
    L = list(palabra)
    for i in range(len(palabra)):
        num = ord(L[i])
        L[i] = chr((num-97+13)%26+97)
            
    palabra = "".join(L)
    return palabra


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           