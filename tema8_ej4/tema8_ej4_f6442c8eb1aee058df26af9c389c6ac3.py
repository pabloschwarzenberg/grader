def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_inicio = ord('a') if letra.islower() else ord('A')
            ascii_letra = ord(letra)
            nueva_letra = chr((ascii_letra - ascii_inicio + 13) % 26 + ascii_inicio)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada en ROT13:", palabra_encriptada)
