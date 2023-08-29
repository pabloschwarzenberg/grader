#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    p1=palabra1
    a=list(palabra1)
    b=list(palabra2)
    for i in p1:
        if i in b:
            b.remove(i)
            a.remove(i)
    l1=len(a)
    l2=len(b)
    if l1>1 or l2>1:
        return "+1"
    elif l1==1 and l2==1:
        return "1S"
    elif (l1==1 and l2==0) or (l1==0 and l2==1):
        return "1B"
    else:
        return "0D"

if __name__=="__main__":
    pass
           