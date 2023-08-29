abc="abcdefghijklmnopqrstuvwxyz"
def rot13 (palabra, contrasena):
    textocifrado=""
    for letra in palabra:
        suma= abc.find(letra) + contrasena
        cifrado= int(suma)
        leN=len(abc)
        textocifrado= textocifrado + str(abc[modulo])
    return textocifrado
           