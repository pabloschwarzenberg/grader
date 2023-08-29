def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_letra = ord(letra)
            if letra.islower():
                nueva_letra = chr((ascii_letra - 97 + 13) % 26 + 97)
            else:
                nueva_letra = chr((ascii_letra - 65 + 13) % 26 + 65)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)

           