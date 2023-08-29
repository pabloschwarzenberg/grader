def rot13(palabra):
    palabra_encriptada = ""

    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                letra_encriptada = chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                letra_encriptada = chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            letra_encriptada = letra

        palabra_encriptada += letra_encriptada

    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
           