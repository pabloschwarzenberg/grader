def rot13(palabra):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    encriptador = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    palabra_rot13 =""
    for letra in palabra:
        elemento= letras.find(letra)
        if elemento <0:
            palpalabra_rot13 += letra
        else:
            palabra_rot13 += encriptador[elemento]

    return palabra_rot13
           