def rot13(palabra):
    palabra_encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_val = ord(letra)
            if letra.islower():
                nueva_letra = chr((ascii_val - 97 + 13) % 26 + 97)
            else:
                nueva_letra = chr((ascii_val - 65 + 13) % 26 + 65)
            palabra_encriptada += nueva_letra
        else:
            palabra_encriptada += letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresar una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
  