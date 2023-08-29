def rot13(palabra):
    primero = "abcdefghijklm"
    segundo = "nopqrstuvwxyz"
    traduccion = ""
    for i in palabra:
        if i in primero:
           posicion = primero.index(i)
           traduccion += segundo[posicion]
        else:
            posicion = segundo.index(i)
            traduccion += primero[posicion]
    pass
    return traduccion
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)