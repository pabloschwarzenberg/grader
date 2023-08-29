#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if (palabra1== palabra2):
        return ("0D")
    elif (len(palabra1))==(len(palabra2)):
        cont=0
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                cont+=1
        if cont==1:
            return ("1S")
    elif (len(palabra1)+1) == (len(palabra2)):
        for i in range(len(palabra2)):
            if (palabra1.count(palabra2[i]))>=1:
                return ("IB")
    elif (len(palabra1)) == (len(palabra2)+1):
        i=0
        while i < len(palabra1):            
            if (palabra2.count(palabra1[i]))>=1:
                i+=1
                return("IB")
            if (palabra2.count(palabra1[i]))==0:
                i+=1
                return("+1")
    elif (len(palabra1)) != (len(palabra2)+1):
        return ("+1")
    elif (len(palabra1)+1) != (len(palabra2)):
        return ("+1")
