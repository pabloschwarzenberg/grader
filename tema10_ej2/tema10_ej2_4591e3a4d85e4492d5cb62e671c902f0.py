#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    Intersection= Inter(palabra1,palabra2)
    if palabra1==palabra2:
        return "0D"
    if len(palabra1)==len(palabra2) and len(Intersection)==2:
        return "1S"
    if abs(len(palabra1)-len(palabra2))==1 and len(Intersection) == 1:
        return "IB"
    else:
        return "+1"
def Inter(p1,p2):
    P1= list(list(p1)+list(p2))
    P2=[]
    for elem in range(len(P1)):
        if P1.count(P1[elem])%2!=0 and P1[elem] not in P2:
            P2.append(P1[elem])
    return P2


if __name__=="__main__":
    pass
           