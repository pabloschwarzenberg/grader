def rot13(palabra):
    lista=""
    for i in palabra:
        letra=ord(i)
        if letra>=ord('a') and letra<=ord('z'):
           if letra>ord('m'):
                letra-=13
           else:
                letra+=13
        elif letra>=ord('A') and letra<=ord('Z'):
           if letra>ord('M'):
                letra-=13
           else:
                letra+=13
        lista += chr(letra)
    return lista

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           