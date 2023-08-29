#La función debe retornar la distancia como un string
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra

def levenshtein(palabra1,palabra2):
    d=0
    if len(palabra1)==len(palabra2):
        for i in range(len(palabra1)):
            if palabra1[i]==palabra2[i]:
                d=d+0
            else:
                d=d+1
                
    elif len(palabra1)>=len(palabra2):
        k=0
        j=0
        while k < len(palabra1):
            for i in range(len(palabra1)):
                if palabra1[i]==palabra2[j]:
                    d=d+0
                    j=j+1
                    k=k+1
                else:
                    d=d+1
                    j=j+0
                    k=k+1
    else:
        k=0
        j=0
        while k < len(palabra2):
            for i in range(len(palabra2)):
                if palabra2[i]==palabra1[j]:
                    d=d+0
                    j=j+1
                    k=k+1
                else:
                    d=d+1
                    j=j+0
                    k=k+1
    if d==0:
        D="0D"
    elif d>1:
        D="+1"
    else:
        if len(palabra1)==len(palabra2):
            D="1S"
        else:
            D="IB"
    return D

           