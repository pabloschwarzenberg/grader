#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    lista=[]
    s=0
    g=0
    if len(palabra1)>=len(palabra2):
        for i in range(0,len(palabra1)-1):
            if lista.count(palabra1[i])==0:
                lista.append(palabra1[i])
                if palabra1.count(palabra1[i])!= palabra2.count(palabra1[i]):
                    s+=1
        if s>1:
            return "+1"
        elif s==1:
            if len(palabra1)!=len(palabra2):
                return "IB"
            if len(palabra1)==len(palabra2):
                return "1S"
        elif s==0 and len(palabra1)==len(palabra2):
            return "0D"
    
    if len(palabra1)<len(palabra2):
        for i in range(0,len(palabra2)-1):
            if lista.count(palabra2[i])==0:
                lista.append(palabra2[i])
                if palabra2.count(palabra2[i])!= palabra1.count(palabra2[i]):
                    g+=1
        if g>1:
            return "+1"
        elif g==1:
            if len(palabra1)!=len(palabra2):
                return "IB"
            if len(palabra1)==len(palabra2):
                return "1S"
        elif g==0 and len(palabra1)==len(palabra2):
            return "0D"
    