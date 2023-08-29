def rot13(word):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    encriptador = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    word_rot13 =""
    for letra in word:
        elemento= letras.find(letra)
        if elemento <0:
            word_rot13 += letra
        else:
            word_rot13 += encriptador[elemento]

    return palabra_rot13