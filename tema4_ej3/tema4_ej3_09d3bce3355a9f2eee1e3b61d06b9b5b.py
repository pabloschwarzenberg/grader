def vocal(string):
    return string in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
def jerigonzo(string):
    cam=""
    for letra in string:
        if not vocal(letra):
            cam+=letra
        else:
            cam+=letra+"p"+letra
    return cam
