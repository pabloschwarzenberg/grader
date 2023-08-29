#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return("0D")
    elif len(palabra1)==len(palabra2):
        i=0
        distancia=0
        while i<len(palabra1):
            if palabra1[i]!=palabra2[i]:
                distancia=distancia+1
            i=i+1
        if distancia==1:
            return("1S")
        if distancia>1:
            return("+1")
    elif (len(palabra1)-len(palabra2))==1 or (len(palabra2)-len(palabra1))==1:
        i=0
        distancia=0
        if len(palabra1)>len(palabra2):
            while i<len(palabra1):
                if palabra1[i] not in palabra2:
                    distancia=distancia+1
                i=i+1
            if distancia>1:
                return("+1")
            if distancia<=1:
                return("IB")
        elif len(palabra2)>len(palabra1):
            while i<len(palabra2):
                if palabra2[i] not in palabra1:
                    distancia=distancia+1
                i=i+1
            if distancia>1:
                return("+1")
            if distancia<=1:
                return("IB")
    else:
        return("+1")
if __name__=="__main__":
    palabra1=input("")
    palabra2=input("")
    print(levenshtein(palabra1,palabra2))
           