def rot13(palabra):
    encriptada = ""
    
    for caracter in palabra:
        if caracter.isalpha():
            ascii_code = ord(caracter)
            if caracter.islower():
                encriptada += chr((ascii_code - 97 + 13) % 26 + 97)
            else:
                encriptada += chr((ascii_code - 65 + 13) % 26 + 65)
        else:
            encriptada += caracter
    
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
