def es_vocal(string):
    return texto in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
def es_vocal(string):
    return string.upper() in ["A", "E", "I", "O", "U"]
def jerigonzo(string):
    variable=""
    for letra in string:
        if not es_vocal(letra):
            variable+=letra
        else:
            variable+=letra+"p"+letra
    return variable
