def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            indice = (ord(caracter) - ord('a') + 13) % 26
            caracter_encriptado = chr(ord('a') + indice)
        elif 'A' <= caracter <= 'Z':
            indice = (ord(caracter) - ord('A') + 13) % 26
            caracter_encriptado = chr(ord('A') + indice)
        else:
            caracter_encriptado = caracter
        resultado += caracter_encriptado
    return resultado
if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    resultado = rot13(palabra)
    print("El resultado es:", resultado)