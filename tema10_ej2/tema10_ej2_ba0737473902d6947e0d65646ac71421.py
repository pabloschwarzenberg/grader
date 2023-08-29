#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    x1=list(palabra1)
    x2=list(palabra2)
    distancia=0
    palabra=0
    a=x1
    if len(x1)>len(x2):
        distancia = distancia + len(x1) - len(x2)
        for i in range(0,len(x2)):
            if palabra1.find(x2[i])!=-1:
                palabra=palabra+1
        x1=x1[0:len(x2)]
        a=x2
    if len(x1) < len(x2):
        distancia = distancia + len(x2) - len(x1)
        for i in range(0,len(x1)):
            if palabra2.find(x1[i])!=-1:
                palabra=palabra+1
        x2 = x2[0:len(x1)]
        a=x1
    comodin=0
    if palabra!=len(x1) and palabra!=len(x2):
        for i in range(0,len(a)):
            if x1[i]!=x2[i]:
                distancia=distancia + 1
                comodin=comodin +1
    if distancia>1:
        return "+1"
    elif abs(palabra-len(palabra1))==1 or abs(palabra-len(palabra2))==1:
        return "IB"
    elif distancia==1 and comodin==1:
        return "1S"
    elif distancia== 0:
        return "0D"

if __name__=="__main__":
    pass
           