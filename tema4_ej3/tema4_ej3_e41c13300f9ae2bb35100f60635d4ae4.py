def jerigonzo(texto):
    vocales=["a","e","i","o","u","á","é","í","ó","ú",
    "A","E","I","O","U","Á","É","Í","Ó","Ú"]
    palabra_texto=""
    for letra in texto:
        if letra in vocales:
            palabra_texto += letra +"p"+ letra
        else:
            palabra_texto += letra
    return (palabra_texto)