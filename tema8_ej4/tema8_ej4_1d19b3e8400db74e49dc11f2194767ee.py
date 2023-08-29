def rot13(palabra):
    palabra_encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            desplazamiento_ascii = ord('a')
            letra_encriptada = chr((ord(letra) - desplazamiento_ascii + 13) % 26 + desplazamiento_ascii)
            palabra_encriptada += letra_encriptada
        else:
            palabra_encriptada += letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)