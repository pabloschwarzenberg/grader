def rot13(palabra):
    lista1 = "abcdefghijklm"
    lista2 = "nopqrstuvwxyz"
    palabratra = ""
    for i in palabra:
        if i in lista1:
            posicion = lista1.index(i)
            palabratra += lista2[posicion]
        else:
            posicion = lista2.index(i)
            palabratra += lista1[posicion]
    pass
    return(palabratra)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           