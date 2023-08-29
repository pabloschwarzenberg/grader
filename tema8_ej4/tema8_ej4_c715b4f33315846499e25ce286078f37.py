def rot13(palabra):
    palabra_encriptada = ""
    
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                codigo = ord(caracter) + 13
                if codigo > ord('Z'):
                    codigo -= 26
                palabra_encriptada += chr(codigo)
            else:
                codigo = ord(caracter) + 13
                if codigo > ord('z'):
                    codigo -= 26
                palabra_encriptada += chr(codigo)
        else:
            palabra_encriptada += caracter
    
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
