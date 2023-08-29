diccionario = {"a": "pa", "e": "pe", "i": "pi", "o": "po", "u": "pu"}
vocales = ["a", "e", "i", "o", "u"]


def jerigonzo(string):
    palabralista = list(string)
    contador = 1
    palabrafinal = []
    for i in palabralista:
        palabrafinal.append(i)
        if i in vocales:
            palabrafinal.append(diccionario[i])
    nueva = "".join(palabrafinal)
    return nueva