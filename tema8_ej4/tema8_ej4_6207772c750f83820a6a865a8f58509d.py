def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                ascii_code = ord(letra) - ord('a')
                nueva_letra = chr((ascii_code + 13) % 26 + ord('a'))
                resultado += nueva_letra
            elif letra.isupper():
                ascii_code = ord(letra) - ord('A')
                nueva_letra = chr((ascii_code + 13) % 26 + ord('A'))
                resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra_ingresada = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra_ingresada)
    print("Palabra encriptada:", palabra_encriptada)