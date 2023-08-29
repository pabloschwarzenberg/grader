def rot13(palabra):
    nueva_palabra = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                nueva_letra = chr((ord(letra)-97+13)%26 + 97)
                nueva_palabra += nueva_letra
            else:
                nueva_letra = chr((ord(letra)-65+13)%26 + 65)
                nueva_palabra += nueva_letra

        else:
            nueva_palabra += letra
    return nueva_palabra

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)
           