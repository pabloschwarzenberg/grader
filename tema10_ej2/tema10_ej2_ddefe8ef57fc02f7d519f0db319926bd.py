#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(a,b):
    if a == b:
        return "0D"
    elif abs(len(a)-len(b)) > 1:
        return "+1"
    elif len(b) == len(a):
        c = []
        for i in range(len(a)):
            if a[i] != b[i]:
                c.append(1)
        if len (c) > 1:
            return "+1"
        else:
            return "1S"
    else:
        if len(b) > len(a):
            d = a
            a = b
            b = d
        for i in range(len(a)):
            c = list(a)
            del c[i]
            c = "".join(c)
            if c == b:
                return "IB"
        return "+1"
        