def rot13(palabra):
    palabra_encriptada  = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                letra_encriptada = chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                letra_encriptada = chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            letra_encriptada = letra
        palabra_encriptada += letra_encriptada
    return palabra_encriptada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)