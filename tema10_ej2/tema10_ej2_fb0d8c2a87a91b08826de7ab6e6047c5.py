#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    n1=len(palabra1)
    n2=len(palabra2)
    if(palabra1==palabra2):
        return "0D"
    elif((n1-n2)>1) or ((n2-n1)>1):
        return "+1"
    elif((n1-n2)==1) or ((n2-n1)==1):
        a1=palabra1[0]
        a2=palabra1[1]
        b1=palabra2[0]
        b2=palabra2[1]
        if(a1==b1)or(a2==b2):
            return "IB"
        else:
            return "+1"
    elif(n1==n2):
        return "1S"


           