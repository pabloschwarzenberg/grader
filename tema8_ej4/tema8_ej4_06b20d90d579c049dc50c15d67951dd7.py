def rot13(palabra):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rot13= "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    cifrado = palabra.translate(palabra.maketrans(normal, rot13))
    return cifrado
                               