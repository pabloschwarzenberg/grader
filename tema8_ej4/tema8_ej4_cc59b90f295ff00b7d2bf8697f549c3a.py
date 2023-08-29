def rot13(palabra):
    return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97)
                    for letter in palabra.lower()])
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           