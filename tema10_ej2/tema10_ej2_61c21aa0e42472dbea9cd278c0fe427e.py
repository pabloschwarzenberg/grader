# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return '0D'
    elif palabra1 != palabra2:
        if len(palabra1) == len(palabra2):
            return '1S'

        elif len(palabra1) > len(palabra2):
            if len(palabra1) - len(palabra2) > 1:
                return '+1'
            else:
                x = list(palabra2)
                x.sort()
                y = list(palabra1)
                y.sort()
                a = 0
                b = 0
                c = 0
                for i in range(0, len(palabra2)):
                    if x[a] == y[b]:
                        a += 1
                        b += 1
                    else:
                        c += 1
                    if c == 2:
                        return '+1'
                return 'IB'

        elif len(palabra1) < len(palabra2):
            if len(palabra2) - len(palabra1) > 1:
                return '+1'
            else:
                x = list(palabra1)
                x.sort()
                y = list(palabra2)
                y.sort()
                a = 0
                b = 0
                c = 0
                for i in range(0,len(palabra1)):
                    if x[a] == y[b]:
                        a += 1
                        b += 1
                    else:
                        c += 1
                    if c == 2:
                        return '+1'
                return 'IB'

if __name__=="__main__":
    pass
           