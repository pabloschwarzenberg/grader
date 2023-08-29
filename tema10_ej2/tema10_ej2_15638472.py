#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    a=0
    h=len(palabra1)
    o=[]
    l=[]
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)==len(palabra2):
        for i in palabra1:
            if i in palabra2:
                a=a+1
        p=h-a
        if p>1:
            return "+1"
        else:
            return "1S"
    elif len(palabra1)>len(palabra2):
        for r in palabra2:
            o+=r
        for i in palabra1:
            if i in o:
                a+=1
                o.remove(i)
        p=h-a
        if p>1:
            return "+1"
        elif p==1:
            return "IB"
    elif len(palabra2)>len(palabra1):
        b=0
        for r in palabra1:
            l+=r
        for i in palabra2:
            if i in l:
                b+=1
                l.remove(i)
        p=len(palabra2)-b
        if p>1:
            return "+1"
        elif p==1:
            return "IB"


if __name__=="__main__":
    pass
           