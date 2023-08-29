#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    if (palabra1==palabra2):
        return "0D"
    distancia = 0
    if (len(palabra1)==len(palabra2)):
        for i in range(0,len(palabra1)):
            if(palabra1[i]!= palabra2[i]):
                distancia += 1
        if (distancia == 1):
            return "1S"
    else:
        if(len(palabra1)<len(palabra2)):
            palabra1, palabra2 = palabra2, palabra1
        diferencia = len(palabra1)-len(palabra2)
        distancia += diferencia
        for i in palabra2:
            if not (i in palabra1):
                distancia += 1
        if (distancia == 1):
            return "IB"

    return "+1"
    pass

if __name__=="__main__":
    pass
           