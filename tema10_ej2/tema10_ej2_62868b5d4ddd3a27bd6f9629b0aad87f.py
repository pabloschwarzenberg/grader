#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    l1 = len(palabra1)
    l2 = len(palabra2)
    contador = 0
    if abs(l1 - l2) >= 2:
        return "+1"
    elif palabra1==palabra2:
        return "0D"
    elif abs(l1 - l2)==0:
        for i in range(l1):
            if palabra1[i]==palabra2[i]:
                continue
            else:
                contador+=1
        if contador > 1:
            return "+1"
        elif contador == 1:
            if abs(l1 - l2) > 0:
                return "IB"
            else:
                return "1S"
    else:
        if l1>l2:
            i=0
            while l1!=l2:
                if palabra1[i]==palabra2[i]:
                    i+=1
                    continue
                else:
                    contador+=1
                    palabra1.pop(i)
                    l1 = len(palabra1)
            for i in range(l1):
                if palabra1[i] == palabra2[i]:
                    continue
                else:
                    contador += 1
            if contador > 1:
                return "+1"
            elif contador == 1:
                if abs(l1+1 - l2) > 0:
                    return "IB"
                else:
                    return "1S"
        elif l1<l2:
            i = 0
            while l1 != l2:
                if palabra1[i] == palabra2[i]:
                    i += 1
                    continue
                else:
                    contador += 1
                    palabra2.pop(i)
                    l2 = len(palabra2)
            for i in range(l1):
                if palabra1[i] == palabra2[i]:
                    continue
                else:
                    contador += 1
            if contador > 1:
                return "+1"
            elif contador == 1:
                if abs(l1 - l2+1) > 0:
                    return "IB"
                else:
                    return "1S"
if __name__=="__main__":
    pass
           