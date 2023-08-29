#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return '0D'
    palabral1=list(palabra1)
    palabral2=list(palabra2)
    if (len(palabral1))!= (len(palabral2))+1 and (len(palabral1))!= (len(palabral2)):
            if (len(palabral1)!=len(palabral2)-1):
                return '+1'
    if (len(palabral1))== (len(palabral2))+1:
        for l in range(len(palabral1)):
            if palabral1[l]!=palabral2[l]:
                palabral1.pop(l)
                if palabral1!=palabral2:
                    return '+1'
                if palabral1==palabral2:
                    return 'IB'
    if (len(palabral1)==len(palabral2)-1):
        for l in range(len(palabral2)):
            if palabral1[l]!=palabral2[l]:
                palabral2.pop(l)
                if palabral1!=palabral2:
                    return '+1'
                if palabral1==palabral2:
                    return 'IB'
    if len(palabra1)==len(palabra2):
        for l in range(len(palabral2)):
            if palabral1[l]!= palabral2[l]:
                palabra1=palabra1.replace(palabra1[l],palabra2[l])
                if palabra1==palabra2:
                    return '1S'

if __name__=="__main__":
    pass
           