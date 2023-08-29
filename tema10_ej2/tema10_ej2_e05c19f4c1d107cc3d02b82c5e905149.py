# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(a, b):
    if a == b:
        return('0D')

    elif len(a) == len(b):
        distancia = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                distancia += 1

        if distancia == 1:
            return('1S')
        else:
            return('+1')

    else:
        distancia = abs(len(a) - len(b))

        if distancia == 1:
            if len(a) < len(b):
                for _a in a:
                    if _a not in b:
                        return('+1')
                else: return 'IB'
            else:
                for _b in b:
                    if _b not in a:
                        return('+1')
                else: return 'IB'
        else:
            return('+1')

if __name__ == "__main__":
    print(levenshtein('jarron', 'melon'))
