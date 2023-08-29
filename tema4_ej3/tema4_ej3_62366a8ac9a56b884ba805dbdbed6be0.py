# Funciones
def jerigonzo(string):
    traducido = []
    vocales = "aeiouáéíóú"
    for x in string:
        traducido.append(x)
        if str(x) in vocales:
            letra = "p" + x
            traducido.append(letra)
    string = "".join(traducido)
    return string

print(jerigonzo("hola"))
