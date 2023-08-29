def es_vocal(text):
    return text.upper() in ["A", "E", "I", "O", "U"]

def jerigonzo(text):
    x=""
    for let in text:
        if not es_vocal(let):
            x+=let
        else:
            x+=let+"p"+let
    return x
