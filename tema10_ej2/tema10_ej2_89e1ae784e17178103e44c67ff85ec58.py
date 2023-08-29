# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)==len(palabra2):
        dif=0
        for i in range(0,len(palabra2)):
            if palabra1[i]!=palabra2[i]:
                dif+=1
        if dif==1:
            return "1S"
        else:
            return "+1"
    elif (len(palabra1)-len(palabra2))>1 or (len(palabra2)-len(palabra1))>1:
        return "+1"
    else:  #IB
        if len(palabra1)<len(palabra2):
            i=0
            j=0
            dif=0
            while i<len(palabra1) and j<len(palabra2):
                if palabra1[i]!=palabra2[j]:
                    dif+=1
                    j+=1
                else:
                    i+=1
                    j+=1
        else:
            k=0
            m=0
            dif=0
            while k<len(palabra2) and m<len(palabra1):
                if palabra2[k]!=palabra1[m]:
                    m+=1
                    dif+=1

                else:
                    k+=1
                    m+=1
        if dif==1:
            return "IB"
        else:
            return "+1"
        pass


if __name__ == "__main__":
    palabra1 = input("Ingrese la palabra 1: ")
    palabra2 = input("Ingrese la palabra 2: ")
    print(levenshtein(palabra1, palabra2))

    pass