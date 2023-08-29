def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            ascii_inicial = ord('a') if letra.islower() else ord('A')
            ascii_letra = ord(letra)
            ascii_encriptado = (ascii_letra - ascii_inicial + 13) % 26 + ascii_inicial
            letra_encriptada = chr(ascii_encriptado)
            resultado += letra_encriptada
        else:
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
