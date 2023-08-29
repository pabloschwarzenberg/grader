def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                resultado += chr((ord(letra) + 13 - 65) % 26 + 65)
            else:
                resultado += chr((ord(letra) + 13 - 97) % 26 + 97)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)
