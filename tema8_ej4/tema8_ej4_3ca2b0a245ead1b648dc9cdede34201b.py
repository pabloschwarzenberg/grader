#ROT13
import string
def rot13(palabra):
    n=13
    mayuscula = string.ascii_uppercase
    minuscula = string.ascii_lowercase
    mayusculaInicio = ord(mayuscula[0])
    minusculaInicio = ord(minuscula[0])
    encriptado = ''
    for letra in palabra:
        if letra in mayuscula:
            encriptado += chr(mayusculaInicio + (ord(letra) - mayusculaInicio + n) % 26)
        elif letra in minuscula:
            encriptado += chr(minusculaInicio+ (ord(letra) - minusculaInicio + n) % 26)
        else:
            encriptado += letra
    return(encriptado)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es:",resultado)