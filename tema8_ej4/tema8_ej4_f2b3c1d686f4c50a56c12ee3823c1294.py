def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                nueva_letra = chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                nueva_letra = chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            nueva_letra = letra
        resultado += nueva_letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
