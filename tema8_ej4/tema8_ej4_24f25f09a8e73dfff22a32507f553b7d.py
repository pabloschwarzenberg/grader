def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                codigo = ord(letra) + 13
                if codigo > ord('z'):
                    codigo -= 26
                resultado += chr(codigo)
            else:
                codigo = ord(letra) + 13
                if codigo > ord('Z'):
                    codigo -= 26
                resultado += chr(codigo)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
