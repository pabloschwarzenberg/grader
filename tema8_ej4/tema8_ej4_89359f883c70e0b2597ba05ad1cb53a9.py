def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    palabra_encriptada = ""
    for letra in palabra:
        if letra.lower() in abecedario:
            indice = (abecedario.index(letra.lower()) + 13) % 26
            letra_encriptada = abecedario[indice]
            if letra.isupper():
                letra_encriptada = letra_encriptada.upper()
            palabra_encriptada += letra_encriptada
        else:
            palabra_encriptada += letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
           