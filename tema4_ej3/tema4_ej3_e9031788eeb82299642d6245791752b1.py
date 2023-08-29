def es_vocal(text):
    return text.upper() in ["A", "E", "I", "O", "U"]

def jerigonzo(text):
    x=""
    for letter in text:
        if not es_vocal(letter):
            x+=letter
        else:
            x+=letter+"p"+letter
    return x
