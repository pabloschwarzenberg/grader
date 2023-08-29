def rot13(palabra):
    palabra_encriptada = ""
    
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.islower():
                nuevo_caracter = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
            else:
                nuevo_caracter = chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
            palabra_encriptada += nuevo_caracter
        else:
            palabra_encriptada += caracter
    
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: {}".format(palabra_encriptada))
