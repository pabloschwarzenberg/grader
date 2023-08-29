#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(p1,p2):
    lp1=len(p1)
    lp2=len(p2)
    if lp2>lp1:
        menor=p1
        mayor=p2
    elif lp1==lp2:
        pass  
    else:
        menor=p2
        mayor=p1
    if p1 == p2:
            return "0D"
    elif lp1==lp2:
        lip1=list(p1)
        lip2=list(p2)
        dis=0
        for i in range(len(lip1)):
            if lip1[i]!=lip2[i]:
                dis+=1
                k=i+1
                if k>=len(lip2):
                    return "1S"
                #borrar o insertar
                else:
                    while k<=len(lip2):
                        if lip1[k] != lip2[k]:
                            dis+=1
                            return "+1"
                        else:
                            return "1S"
            else:
                pass
    else:
        lime=list(menor)
        lima=list(mayor)
        dis=0
        for i in range(len(lime)):
            if lime[i]!=lima[i]:
                dis+=1
                k=i+1
                #borrar o insertar
                while k<=len(lima):
                    if lime[i] != lima[k]:
                        dis+=1
                        return "+1"
                    else:
                        return "IB"
            else:
                pass
                    
if __name__=="__main__":
    levenshtein("caro", "cara")
           