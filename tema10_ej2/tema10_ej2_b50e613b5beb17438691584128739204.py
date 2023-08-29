#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales


def levenshtein(p1,p2):
    x = len(p1)
    y = len(p2)

    if x == y:
        if p1 == p2:
            z = "0D"
        else:

            diferentes = 0
            i = 0
            while i < x:
                if p1[i] != p2[i]:
                    diferentes = diferentes + 1
                i = i + 1
            if diferentes > 1 :
                z = "+1"
            else:
                z = "1S"
    else:
        if x > y :
            mayor = p1
            menor = p2
        elif x < y:
            mayor = p2
            menor = p1
        if (len(mayor) - len(menor)) == 1:
            z = "IB"
        else:
            z = "+1"


    return z