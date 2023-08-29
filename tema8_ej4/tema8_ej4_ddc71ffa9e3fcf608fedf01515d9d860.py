def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            nuevocaracter = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= caracter <= 'Z':
            nuevocaracter = chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            nuevocaracter = caracter
        resultado += nuevocaracter
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           