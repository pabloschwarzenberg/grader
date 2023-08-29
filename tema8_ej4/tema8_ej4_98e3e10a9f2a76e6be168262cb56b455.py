def rot13(frase):
    traducida = ""
    original = "ABCDEFGHIJKLM"
    cambio = "NOPQRSTUVWXYZ"
    for letra in frase:
        traducida = traducida+letra
        if letra.lower() in "ABCDEFGHIJKLM":
            traducida = traducida + "NOPQRSTUVWXYZ" + letra
    return traducida
    