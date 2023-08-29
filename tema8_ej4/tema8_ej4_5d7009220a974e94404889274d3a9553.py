def rot13(palabra):
    a = ''
    for i in palabra:
        b = ord(i)
        if (b >= 65 and b <= 90) or (b >= 97 and b <= 122):
            if ((b + 13 > 90 and b + 13 <= 103) or (b + 13 > 122 and b + 13 <= 135)):
                a += chr(b -13)
            else:
                a += chr(b + 13)
    return a

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           