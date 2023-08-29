#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
        n=0
        i=0
        for i in range(len(palabra1)):
            if palabra1[i]==palabra2[i]:
                continue
            if palabra1[i]!=(palabra2[i]):
                n+=1
        if n>1:
            return "+1"
        if n==1:
            return "1S"
        if n==0:
            return "0D"
    if abs(len(palabra1)-len(palabra2))>=2:
        return "+1"
    else:
        if len(palabra1)>len(palabra2):       
                    
            x=list(palabra1)
            for i in range(len(palabra2)):
                if palabra2[i] in x:
                    x.remove(palabra2[i])
            if len(x)==abs(len(palabra1)-len(palabra2)):
                if len(x)==1:
                    return "IB"
                else:
                    return "+1"
            else:
                return "+1"
        if len(palabra1)<len(palabra2):       
                    
            x=list(palabra2)
            for i in range(len(palabra1)):
                if palabra1[i] in x:
                    x.remove(palabra1[i])
            if len(x)==abs(len(palabra1)-len(palabra2)):
                if len(x)==1:
                    return "IB"
                else:
                    return "+1"
            else:
                return "+1"
if __name__=="__main__":
    pass
           