def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            ascii_offset = 65 if letra.isupper() else 97
            encriptado = chr((ord(letra) - ascii_offset + 13) % 26 + ascii_offset)
            resultado += encriptado
        else:
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
