def rot13(palabra):
    Cifrado = ''
    for i in palabra:
        letras = ord(i)
        if (letras >= 65 and letras <= 90) or (letras >= 97 and letras <= 122):
            if ((letras + 13 > 90 and letras + 13 <= 103) or (letras + 13 > 122 and letras + 13 <= 135)):
                Cifrado += chr(letras -13)
            else:
                Cifrado += chr(letras + 13)
    return Cifrado
   

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           