def rot13(palabra):
    resultado = ""
    for char in palabra:
        if char.isalpha():
            if char.islower():
                codigo = ord(char) + 13
                if codigo > ord("z"):
                    codigo -= 26
                resultado += chr(codigo)
            else:
                codigo = ord(char) + 13
                if codigo > ord("Z"):
                    codigo -= 26
                resultado += chr(codigo)
        else:
            resultado += char
    return resultado

if __name__ == "_main_":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)