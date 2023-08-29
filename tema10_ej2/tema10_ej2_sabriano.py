#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
import math
def levenshtein(palabra1,palabra2):
    distancia=0
    lista1=list(palabra1)
    lista2=list(palabra2)
    if len(palabra1)>len(palabra2):
        for i in lista2:
            if i not in lista1:
                distancia+=1
    elif len(palabra2)>=len(palabra1):
        for i in lista1:
            if i not in lista2:
                distancia+=1
    distancia+=math.fabs(len(palabra1)-len(palabra2))

    if distancia>1:
        return "+1"
    elif distancia==1 and len(palabra1)==len(palabra2):
        return"1S"
    elif distancia==0:
        return "0D"
    elif distancia==1 and len(palabra1)!=len(palabra2):
        return "IB"

if __name__=="__main__":
    pass
           