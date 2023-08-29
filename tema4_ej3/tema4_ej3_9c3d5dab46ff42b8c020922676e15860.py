def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def es_vocal(texto):
    return texto.upper() in ["A", "E", "I", "O", "U"]

def jerigonzo(texto):
    x=""
    for letra in texto:
        if not es_vocal(letra):
            x+=letra
        else:
            x+=letra+"p"+letra
    return x         