def jerigonzo(string):
    def es_vocal(string):
        return string.upper() in ["A", "E", "I", "O", "U"]
    aux=''
    for letra in string:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux


if __name__ == "__main__":
    pass
         