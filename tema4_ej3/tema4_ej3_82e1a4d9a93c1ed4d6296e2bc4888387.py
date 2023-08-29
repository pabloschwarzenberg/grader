def jerigonzo(texto):
    textoJerigonzo = ''
    for letra in texto:
        textoJerigonzo += letra
        for vocal in 'aeiou':
            if letra == vocal:
                textoJerigonzo += 'p' + vocal

    return textoJerigonzo