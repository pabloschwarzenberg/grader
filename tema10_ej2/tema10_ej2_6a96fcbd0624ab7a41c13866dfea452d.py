#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if len1 == len2:
        distancia = sum(c1 != c2 for c1, c2 in zip(palabra1, palabra2))
        if distancia > 1:
            return "+1"
        elif distancia == 1:
            return "1S"
        else:
            return "0D"
    elif abs(len1 - len2) == 1:
        if len1 < len2:
            palabra1, palabra2 = palabra2, palabra1
            len1, len2 = len2, len1
        for i in range(len2):
            if palabra1[:i] + palabra1[i+1:] == palabra2:
                return "IB"
        return "+1"
    else:
        return "+1"


if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
