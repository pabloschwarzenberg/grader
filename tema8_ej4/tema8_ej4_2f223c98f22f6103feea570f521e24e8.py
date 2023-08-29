def rot13(palabra):
    encriptada = ""
    
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                encriptada += chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
            else:
                encriptada += chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        else:
            encriptada += caracter
    
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           