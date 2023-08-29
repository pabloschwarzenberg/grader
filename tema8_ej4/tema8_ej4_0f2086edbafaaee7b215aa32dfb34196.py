def rot13(palabra):
    resultado = ""
    palabra=palabra.lower()
    for v in palabra:
        c = ord(v)
        if c > ord('m'):
            c = c-13
        else:
            c = c + 13
        resultado = resultado + chr(c)

    return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           