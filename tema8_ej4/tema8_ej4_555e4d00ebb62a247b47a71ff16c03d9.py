def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                codigo = ord(letra) - 65
                nueva_letra = chr((codigo + 13) % 26 + 65)
            else:
                codigo = ord(letra) - 97
                nueva_letra = chr((codigo + 13) % 26 + 97)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           