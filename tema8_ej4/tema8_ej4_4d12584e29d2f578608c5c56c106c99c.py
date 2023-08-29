def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                resultado += chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                resultado += chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = "Hola, mundo!"
    palabra_encriptada = rot13(palabra)
    print(palabra_encriptada)  # Ubyn, zhaqb!
           