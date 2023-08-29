def rot13(palabra):
    decodif = ""


    for i in palabra:
        cordenada = ord(i)


        if cordenada >= ord('a') and cordenada <= ord('z'):
            if cordenada > ord('m'):
                cordenada -= 13
            else:
                cordenada += 13

        elif cordenada >= ord('A') and cordenada <= ord('Z'):
            if cordenada > ord('M'):
                cordenada -= 13
            else:
                cordenada += 13


        decodif += chr(cordenada)


    return decodif

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
