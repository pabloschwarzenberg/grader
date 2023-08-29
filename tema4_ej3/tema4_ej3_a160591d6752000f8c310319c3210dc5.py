def jerigonzo(string):
    string.lower()
    vocalJeri=""
    stringJeri=""
    for letra in string:
        if ord(letra)==97:
            vocalJeri=letra+"pa"
        elif ord(letra)==101:
            vocalJeri=letra+"pe"
        elif ord(letra)==105:
            vocalJeri=letra+"pi"
        elif ord(letra)==111:
            vocalJeri=letra+"po"
        elif ord(letra)==117:
            vocalJeri=letra+"pu"
        else:
            vocalJeri=letra
        stringJeri+=vocalJeri
    return stringJeri
         