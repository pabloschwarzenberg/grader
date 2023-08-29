def es_vocal(string):
    return string in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def es_vocal(string):
    return string.upper() in ["A", "E", "I", "O", "U"]

def es_vocal(string):
    return string.upper() in "AEIOU" and len(string)==1
    
def jerigonzo(string):
    aux=""
    for letra in string:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux