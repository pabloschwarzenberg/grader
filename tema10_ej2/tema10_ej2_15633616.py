#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein (palabra1,palabra2):
    listaf=[]
    j=0
    i=0
    if len(palabra1)==len(palabra2):
        while i<len(palabra1):
            if palabra1[i]!=palabra2[i]:
                j+=1
            i+=1
        if j==0:
            return ("0D")
        if j==1:
            return("1S")
        if j>1:
            return ("+1")
    else:
        if (len(palabra1)-len(palabra2))>1 or (len(palabra2)-len(palabra1))>1:
            return ("+1")
            
        lista1=list(palabra1)
        lista2=list(palabra2)
        i=0
        if len(lista1)>len(lista2):
            while i<len(lista1):
                if lista1[i]!=lista2[i]:
                    listaf.append(lista1[i])
                    lista1.pop(i)
                    break   
                else:
                    i+=1
            i=0
            while i<len(lista1):
                if lista1[i]!=lista2[i]:
                    listaf.append(lista1[i])
                i+=1
        if len(lista2)>len(lista1):
            while i<len(lista2):
                if lista1[i]!=lista2[i]:
                    listaf.append(lista1[i])
                    lista2.pop(i)
                    break   
                else:
                    i+=1
            i=0
            while i<len(lista2):
                if lista1[i]!=lista2[i]:
                    listaf.append(lista2[i])
                i+=1
        
                    
            
        if len(listaf)==1:
            return("IB")
        if len(listaf)>1:
            return ("+1")


if __name__=="__main__":
    pass
           