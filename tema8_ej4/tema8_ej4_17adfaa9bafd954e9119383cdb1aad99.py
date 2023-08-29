def rot13(palabra):
    palabra_encriptada = ""
    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            indice = (ord(caracter) - ord('a') + 13) % 26
            caracter_encriptado = chr(ord('a') + indice)
        elif 'A' <= caracter <= 'Z':
            indice = (ord(caracter) - ord('A') + 13) % 26
            caracter_encriptado = chr(ord('A') + indice)
        else:
            caracter_encriptado = caracter
        palabra_encriptada += caracter_encriptado
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
