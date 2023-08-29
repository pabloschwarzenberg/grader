def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                codigo = (ord(letra) - ord('A') + 13) % 26 + ord('A')
                resultado += chr(codigo)
            else:
                codigo = (ord(letra) - ord('a') + 13) % 26 + ord('a')
                resultado += chr(codigo)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
