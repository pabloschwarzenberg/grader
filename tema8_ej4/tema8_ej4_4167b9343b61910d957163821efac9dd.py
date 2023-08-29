def rot13(palabra):
    palabra_encriptada = ''
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                nueva_letra = chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                nueva_letra = chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            nueva_letra = letra
        palabra_encriptada += nueva_letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra_original = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra_original)
    print("Palabra encriptada: ", palabra_encriptada)
