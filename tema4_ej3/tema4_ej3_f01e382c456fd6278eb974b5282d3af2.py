def jerigonzo(texto):
    aux=""
    for letra in texto:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux