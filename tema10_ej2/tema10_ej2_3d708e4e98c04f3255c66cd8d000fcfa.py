# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    count = 0
    if palabra1 == palabra2:
        return "0D"
    elif len(palabra1) == len(palabra2):
        for x in palabra1:
            if x not in palabra2:
                count += 1
        if count > 0:
            return "1S"
    elif len(palabra1) != len(palabra2):
        delta = abs(len(palabra1) - len(palabra2))
        for x in palabra1:
            if x not in palabra2:
                count += 1
        if delta > 1 or count > 1:
            return "+1"
        else:
            return "IB"


if __name__ == "__main__":
    p1 = input()
    p2 = input()
    print(levenshtein(p1, p2))
