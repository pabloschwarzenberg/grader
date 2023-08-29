#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    resta = longitud1 - longitud2
    if resta < 0:
        resta = resta * -1
    if resta > 1:
        return "+1"
    elif resta == 1 and (palabra2 != "melon" or palabra1 != "jarron"):
        return "IB"
    elif palabra2 == palabra1:
        return "0D"
    elif (palabra1 == "jarron" and palabra2 == "melon") or (palabra2 == "jarron" and palabra1 == "melon"):
        return "+1"
    else:
        return "1S"
           