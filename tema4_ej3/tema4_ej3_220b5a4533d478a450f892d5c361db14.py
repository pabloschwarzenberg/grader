#transformar mayusculas#
def es_vocal(text):
    return text.upper() in ["A", "E", "I", "O", "U"]
#funcion jeringozo#
def jerigonzo(text):
    a=""
    for let in text:
        if not es_vocal(let):
            a+=let
        else:
            a+=let+"p"+let
    return a