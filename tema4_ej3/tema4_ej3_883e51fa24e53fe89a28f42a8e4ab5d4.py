def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouáéíóú"
    
    for letra in texto:
        jerigonzo += letra
        if letra.lower() in vocales:
            jerigonzo += "p" + letra.lower()
    
    return jerigonzo("estamos programando")