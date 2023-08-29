#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(p1,p2):
    if p1==p2:
        return "0D"
    elif len(p1)==(len(p2)-1):
        i=0
        while i<len(p1):
            if p2.find(p1[i])!=-1:
                return "IB"
            else:
                return "+1"
    elif len(p2)==(len(p2)-1):
        i=0
        while i<len(p2):
            if p1.find(p2[i])!=-1:
                return "IB"
            else:
                return "+1"
    elif len(p1)==len(p2):
        contador=[]
        i=0
        while i<len(p2):
            c=p2[i]
            if p1.find(c)!=-1:
                contador.append(1)
                p1=p1.replace(p2[i],"",1)
            i+=1
        if len(contador)==(len(p2)-1):
            return "1S"
        elif len(contador)<(len(p2)-1):
            return "+1"
    else:
        return "+1"
    
        

if __name__=="__main__":
    p1=input("1: ")
    p2=input("2: ")
    print(levenshtein(p1,p2))
