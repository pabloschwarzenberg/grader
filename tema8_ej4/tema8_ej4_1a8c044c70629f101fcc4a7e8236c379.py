def rot13(palabra):
    alfabeto_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    alfabeto_encriptado = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    palabra_encriptada = ""
    for letra in palabra:
        if letra in alfabeto_original:
            indice = alfabeto_original.index(letra)
            letra_encriptada = alfabeto_encriptado[indice]
            palabra_encriptada += letra_encriptada
        else:
            palabra_encriptada += letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
