#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    global contador
    contador = 0
    if palabra1 == palabra2:
        return "0D"
    elif len(palabra1) == len(palabra2) + 1:
        for i in range(0,len(palabra2)):
            if palabra2[0:i] == palabra1[0:i] and palabra2[i:] == palabra1[i+1:]:
                return "IB"
            else:
                contador += 1
        if contador == len(palabra2):
            return "+1"
    elif len(palabra2) == len(palabra1) + 1:
        for i in range(0,len(palabra1)):
            if palabra1[0:i] == palabra2[0:i] and palabra1[i:] == palabra2[i+1:]:
                return "IB"
            else:
                contador += 1
        if contador == len(palabra1):
            return "+1"
    elif len(palabra2) == len(palabra1):
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                contador += 1
        if contador == 1:
            return "1S"
        else:
            return "+1"
    else:
        return "+1"