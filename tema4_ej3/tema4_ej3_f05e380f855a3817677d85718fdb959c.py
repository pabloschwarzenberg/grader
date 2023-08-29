def jerigonzo(text):
    c=""
    for o in text:
        if not es_vocal(o):
            c+=o
        else:
            c+=o+"p"+o
    return c
def es_vocal(text):
    return text.upper() in ["A", "E", "I", "O", "U"]