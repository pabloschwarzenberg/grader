#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    lis1 = []
    lis2 = []
    con1 = 0
    for i in palabra1:
        lis1.append(i)
    for j in palabra2:
        lis2.append(j)
    lis1.sort()
    lis2.sort()
    if len(lis1) == len(lis2):
        for a in range(len(lis1)):
            if lis1[a] == lis2[a]:
                con1 += 1
        if con1 == len(lis1) and con1 == len(lis2):
            return "0D"
        else:
            return "1S"
    
    if len(palabra1) > len(palabra2) or\
       len(palabra1) < len(palabra2):
        if len(palabra1) > len(palabra2):
            for a in palabra1:
                if a not in lis2:
                    con1+=1
            if (con1 == 1 or con1 == 0) and (len(palabra1)-len(palabra2) == 1 or\
                             len(palabra1)-len(palabra2) == -1):
                return "IB"
            else:
                return "+1"
        if len(palabra1) < len(palabra2):
            for a in palabra2:
                if a not in lis1:
                    con1+=1
            if (con1 == 1 or con1 == 0) and (len(palabra1)-len(palabra2) == 1 or\
                             len(palabra1)-len(palabra2) == -1):
                return "IB"
            else:
                return "+1"
                
                
                    
        
        
la = levenshtein("jarron","jaron")
print(la)


if __name__=="__main__":
    pass
           