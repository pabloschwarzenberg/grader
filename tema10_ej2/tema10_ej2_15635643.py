#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
import math
def levenshtein(palabra1,palabra2):
    letras1=list(palabra1)
    letras2=list(palabra2)
    sust=False
    distancia=0
    if len(palabra1)>len(palabra2):
        for letra in letras2:
            if letra not in letras1:
                distancia+=1
    elif len(palabra1)<=len(palabra2):
        for letra in letras1:
            if letra not in letras2:
                distancia+=1

    distancia+=int(math.fabs(len(palabra1)-len(palabra2)))

    if distancia>1:
        return "+1"
    elif distancia==0:
        return "0D"
    elif distancia==1 and len(palabra1)==len(palabra2):
        return "1S"
    elif distancia==1 and len(palabra1)!=len(palabra2):
        return "IB"
if __name__=="__main__":
    pass
           