#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    lar1 = len(palabra1)
    lar2 = len(palabra2)
    pal1 = []; pal2 = []
    pal1 = pal1+ list(palabra1)
    pal2 = pal2+ list(palabra2)
    j = 0;  k = 0; count = 0
    while j < len(palabra1):
        if k == lar2:
            break
        if pal1[j] == pal2[k]:
            j = j + 1
            k = j
        else:
            j = j
            k = k + 1
            count = count + 1   
    if palabra1 == palabra2:
        d = "0D"
    elif (lar2 - lar1) == 1 and count==2:
        d = "IB"
    elif lar1 != lar2:
        d = "+1"
    elif lar1 == lar2 and count>=1:
        d = "1S"
    return d
