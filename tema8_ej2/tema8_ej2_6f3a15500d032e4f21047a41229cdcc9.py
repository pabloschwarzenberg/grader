def buscarTodas(a,b):
    pass

if __name__ == "__main__":
    pass
def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_code = ord(letra) - ord('A')
                nueva_letra = chr((ascii_code + 13) % 26 + ord('A'))
            else:
                ascii_code = ord(letra) - ord('a')
                nueva_letra = chr((ascii_code + 13) % 26 + ord('a'))
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
