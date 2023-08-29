#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    i = 0
    j = 0
    d=0
    if (palabra1 == palabra2):
        return ("0D")
    elif (len(palabra1) > len(palabra2)):

        while (i < len(palabra1)):

            if (len(palabra2) > i):
                if (palabra1[i] == palabra2[i]):
                    i = i + 1

                elif (palabra1[i] != palabra2[i]):
                    i = i + 1
                    j = j + 1

            if (i >= len(palabra2)):

                i = i + 1
                d=d+1
    elif (len(palabra2) > len(palabra1)):

        while (i < len(palabra2)):

            if (len(palabra1) > i):
                if (palabra1[i] == palabra2[i]):
                    i = i + 1

                elif (palabra1[i] != palabra2[i]):
                    i = i + 1
                    j = j + 1

            if (i >= len(palabra1)):

                i = i + 1
                d=d+1
    elif (len(palabra2)==len(palabra1)):
        while(i<len(palabra1)):
            if(palabra1[i]==palabra2[i]):
                i=i+1
            elif(palabra1[i]!=palabra2[i]):
                i=i+1
                j=j+1


    if (d == 1):
        if(j==2):
            return ("IB")
        if(j>2):
            return ("+1")
    if (len(palabra1) == len(palabra2)) and (j == 1):
        return ("1S")
   
    if(d>1):
        return("+1")

