def rot13(palabra):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    palabrarot13 = ''
    for letra in palabra:
        posicion = letras.find(letra)
        if posicion < 0:
            palabrarot13 += letra
        else:
            palabrarot13 += rot13[posicion]
    
    return palabrarot13
           