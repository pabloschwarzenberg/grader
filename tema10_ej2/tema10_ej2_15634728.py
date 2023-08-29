#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    l1 = list(palabra1)
    l2 = list(palabra2)
    if palabra1 == palabra2:
        return "0D"
    if abs(len(l1)-len(l2)) == 1:
        iguales = False
        for i in range(min(len(l1),len(l2))):
            if l1[i] != l2[i]:
                if len(l1)>len(l2):
                    l1.pop(i)
                else:
                    l2.pop(i)
                if l1 == l2:
                    return "IB"
                else:
                    return "+1"
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                l1.pop(i)
                l2.pop(i)
                if l1 == l2:
                    return "1S"
                else:
                    return "+1"
    else:
        return "+1"
        

if __name__=="__main__":
    pass
           