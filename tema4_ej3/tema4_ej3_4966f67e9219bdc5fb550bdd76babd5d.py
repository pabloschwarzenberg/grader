def jerigonzo(texto):
    traduccion = []
    for i in texto:
        for letra in i:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            traduccion.append(letra)
    traduccion = "".join(traduccion)
    return traduccion