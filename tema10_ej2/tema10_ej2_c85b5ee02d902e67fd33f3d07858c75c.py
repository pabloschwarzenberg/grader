#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass

if __name__=="__main__":
    pass
def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"
    elif palabra1 == palabra2:
        return "0D"
    elif len1 == len2:
        distancia = sum(palabra1[i] != palabra2[i] for i in range(len1))
        if distancia == 1:
            return "1S"
    elif abs(len1 - len2) == 1:
        if len1 > len2:
            palabra1, palabra2 = palabra2, palabra1
            len1, len2 = len2, len1
        i = j = distancia = 0
        while i < len1 and j < len2:
            if palabra1[i] != palabra2[j]:
                distancia += 1
                if distancia > 1:
                    return "+1"
                if len1 != len2:
                    i -= 1
            i += 1
            j += 1
        return "IB"
    
    return "+1"
          