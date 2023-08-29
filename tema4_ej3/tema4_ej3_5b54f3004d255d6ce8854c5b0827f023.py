def jerigonzo(texto):
    aux=""
    for letra in texto:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux


def es_vocal(texto):
    return texto in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def es_vocal(texto):
    return texto.upper() in ["A", "E", "I", "O", "U"]

def es_vocal(texto):
    return texto.upper() in "AEIOU" and len(texto)==1


