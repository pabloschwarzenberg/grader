def rot13(palabra):
    encriptado=""
    i=0
    while i<len(palabra):
        if palabra[i]<"n":
            letra=chr(ord(palabra[i])+13)
            encriptado=encriptado+letra
            i=i+1
        elif palabra[i]>="n":
            letra = chr(ord(palabra[i]) - 13)
            encriptado = encriptado + letra
            i=i+1


    return encriptado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra=palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           