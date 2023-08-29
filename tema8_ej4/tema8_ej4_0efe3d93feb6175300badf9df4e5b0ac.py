def rot13(palabra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encriptada = ''

    for letra in palabra:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) + 13) % 26
            encriptada += alfabeto[indice]
        else:
            encriptada += letra

    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)

