def rot13(palabra):
    resultado = ''
    for letra in palabra:
        if letra <= 'm':
            resultado += chr(ord(letra) + 13)
        else:
            resultado += chr(ord(letra) - 13)
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
           