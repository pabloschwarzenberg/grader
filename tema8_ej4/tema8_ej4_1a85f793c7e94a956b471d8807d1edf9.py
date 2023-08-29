def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                nueva_letra = chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                nueva_letra = chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: {}".format(palabra_encriptada))
