#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(string1,string2):
    if string1==string2:
        return("0D")
    else:
        lista1=list(string1)
        lista2=list(string2)
        largo1=len(lista1)
        largo2=len(lista2)
        if largo1>largo2:
            for i in range(largo1):
                if lista1[i]!=lista2[i]:
                    lista1.pop(i)
                    break
            z="".join(lista1)
            if z in string2:
                distancia=largo1-largo2
                if distancia==1:
                    return("1I/B")
                elif distancia==0:
                    return("1S")
                else:
                    return("+1")
            else:
                return("+1")
                
        else:
            for i in range(largo2):
                if lista2[i]!=lista1[i]:
                    lista2.pop(i)
                    break
            z="".join(lista2)
            if z in string1:
                distancia=largo2-largo1
                if distancia==1:
                    return("IB")
                elif distancia==0:
                    return("1S")
                else:
                    return("+1")
            else:
                return("+1")

if __name__=="__main__":
    pass
           