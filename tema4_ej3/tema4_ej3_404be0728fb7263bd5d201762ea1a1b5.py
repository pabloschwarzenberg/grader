def jerigonzo(frase):
    agrega = ""
    for letra in frase:
        if letra in "AEIOUaeoiu":
            agrega += letra
            agrega += "p"
        agrega +=letra
    return agrega