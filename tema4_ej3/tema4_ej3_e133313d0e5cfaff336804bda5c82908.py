def jerigonzo(string):
    texto = ""
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    for n in string:
        if n in consonantes:
            texto += n
        if n in vocales:
            texto += n+"p"+n
        if n == " ":
            texto += " "
        
    return texto

         