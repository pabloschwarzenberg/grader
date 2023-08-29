#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    h=0
    if abs(len(palabra1)-len(palabra2))>1:
        return "+1"
    if abs(len(palabra1)-len(palabra2))==1:
         for i in range(0,len(palabra1)):
          if palabra1[i]!=palabra2[i]:
             h+=1
    if h>1:
        return "+1"
    return "IB"
    if len(palabra1)==len(palabra2):
        if palabra1 == palabra2:
            return "0D"
        else:
            return "1S"



           