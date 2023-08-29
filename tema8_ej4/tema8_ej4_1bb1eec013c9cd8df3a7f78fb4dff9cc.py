def rot13(palabra):
    Cifrado = ''
    for i in palabra:
        buff = ord(i)
        if (buff >= 65 and buff <= 90) or (buff >= 97 and buff <= 122):
            if ((buff + 13 > 90 and buff + 13 <= 103) or (buff + 13 > 122 and buff + 13 <= 135)):
                Cifrado += chr(buff - 13)
            else:
                Cifrado += chr(buff + 13)
    return Cifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           