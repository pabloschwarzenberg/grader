def rot13(palabra):
    resultado=""

    for i in palabra:
        
        x  = ord(i)


        if x >= ord('a') and x <= ord('z'):
            if x > ord('m'):
                x -= 13
            else:
                x += 13
        elif x >= ord('A') and x <= ord('Z'):
            if x > ord('M'):
                x -= 13
            else:
                x += 13

        
        resultado += chr(x)


    return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           