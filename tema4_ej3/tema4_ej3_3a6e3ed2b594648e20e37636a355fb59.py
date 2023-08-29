def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u" ]
    pal = ""
    for tex in string:     
        if tex in vocales:
            pal += tex
            pal += "p"
            pal += tex
        else:
            pal += tex     
    return pal
         