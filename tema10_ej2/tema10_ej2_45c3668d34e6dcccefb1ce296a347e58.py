#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(p_1,p_2):
    a=len(p_1)
    b=len(p_2)
    c=a-b
    if c<-1 or c>=1:
        return "+1"
    if c==1 or c==-1:
        return "IB"

    if c==0:
        if p_1==p_2:
            return "0D"
        else:
            return "1S"

           