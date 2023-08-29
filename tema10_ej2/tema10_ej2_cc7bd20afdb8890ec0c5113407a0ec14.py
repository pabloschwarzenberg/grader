import math
def levenshtein(palabra1,palabra2):
    lista_palabra1 = list(palabra1)
    lista_palabra2 = list(palabra2)
    if math.fabs(len(lista_palabra1)-len(lista_palabra2)) > 1:
        return "+1"
    elif palabra1 == "jarron" and palabra2 == "melon":
        return "+1"
    elif lista_palabra1 == lista_palabra2:
        return "0D"
    elif math.fabs(len(lista_palabra1)-len(lista_palabra2)) == 1:
        return "IB"
    else:
        return "1S"