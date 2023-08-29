#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if(abs(len(palabra1)-len(palabra2))>1):
        return "+1"
    if(abs(len(palabra1)-len(palabra2))==1):
        if ((palabra1 in palabra2)or(palabra2 in palabra1)):
            return "IB"
    if(abs(len(palabra1)-len(palabra2))==0):
        if(palabra1==palabra2):
            return "0D"
        i=0
        a=0
        while i<len(palabra1):
            l1=list(palabra1)
            l2=list(palabra2)
            if l1[i]==l2[i]:
                a=a+1
            i=i+1
        if(len(palabra1)-a>1):
            return "+1"
        else:
            return "1S"

if __name__=="__main__":
    pass
           