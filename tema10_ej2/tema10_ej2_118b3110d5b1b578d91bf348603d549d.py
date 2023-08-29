#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    if max(len(palabra1),len(palabra2))-2>= min(len(palabra1),len(palabra2)):
        k = 0
        for u in range(min(len(palabra1),len(palabra2))):
            if palabra1[u]!=palabra2[u]:
                k += 1
        if k==0:
            return "+1"
        else:
            return "+1"
    elif max(len(palabra1),len(palabra2))-1== min(len(palabra1),len(palabra2)):
        k = 0
        for u in range(min(len(palabra1),len(palabra2))):
            if palabra1[u]!=palabra2[u]:
                k += 1
        if k<=2:
            return "IB"
        elif k>2:
            return "+1"
    elif max(len(palabra1),len(palabra2))== min(len(palabra1),len(palabra2)):
        if palabra1==palabra2:
            return "0D"
        else:
            for i in range(len(palabra1)):
                if palabra1[i]!=palabra2[i]:
                    return "1S"