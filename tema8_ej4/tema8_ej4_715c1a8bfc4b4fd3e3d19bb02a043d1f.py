#Cifrado cesar
def rot13(palabra):
    resultado = ""
    
    for caracter in palabra:
        if caracter.isalpha():
            ascii_original = ord(caracter.lower())
            ascii_encriptado = (ascii_original - 97 + 13) % 26 + 97
            caracter_encriptado = chr(ascii_encriptado)
            
            if caracter.isupper():
                caracter_encriptado = caracter_encriptado.upper()
            
            resultado += caracter_encriptado
        else:
            resultado += caracter
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           