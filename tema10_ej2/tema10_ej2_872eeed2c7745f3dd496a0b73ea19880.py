#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):

    p1=palabra1

    p2=palabra2

    l1=len(p1)

    l2=len(p2)

    if p1==p2:

        return "0D"

    if l1==l2:

        i=0

        s=""

        while i<len(p1):

            a=p1[i]

            r= a in p2

            if r==True:

                s=s+a

            i=i+1

        if (len(p2)-len(s))==1:

            return "1S"

        elif (len(p2)-len(s))>1:

            return "+1"


    if l1!=l2:

        i=0

        s=""

        while i<len(p1):

            a=p1[i]

            r= a in p2

            if r==True:

                s=s+a

            i=i+1

        if (len(p2)-len(s))==1:

            return "IB"

        elif (len(p2)-len(s))>1:

            return "+1"

if __name__=="__main__":
    pass
           