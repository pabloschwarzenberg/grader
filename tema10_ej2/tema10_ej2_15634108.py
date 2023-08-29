#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    p1=list(palabra1)
    p2=list(palabra2)
    T1=len(p1)
    T2=len(p2)
    if T1==T2:
        i=0
        r=0
        while i<T1:
            if p1==p2:
                return "0D"
            elif p1[i]==p2[i]:
                r=r
            elif p1[i]!=p2[i]:
                r+=1
            r=r
            i+=1
        if r==1:
            return "1S"
        elif r>1:
            return "+1"
    elif T1>T2:
        if T1>T2+1:
            return "+1"
        elif palabra2 in palabra1:
            if True:
                return "IB"
        else:
            q=0
            e=0
            while q<T2:
                if p1[q]==p2[q]:
                    e=e
                elif p1[q]!=p2[q]:
                    u=0
                    while u<T2:
                       k=palabra1.find(p2[u])
                       if k==-1:
                           e+=1
                           u+=1
                       else:
                           e=e
                           u+=1
                q+=1
            if e==1:
                return "1S"
            elif e>1:
                return "+1"
    elif T2>T1:
        if T2>T1+1:
            return "+1"
        elif palabra1 in palabra2:
            if True:
                return "IB"
        elif T2==T1+1:
            x=0
            f=0
            while x<T1:
                if p2.count(p1[x])>0:
                    f+=1
                    x+=1
                else:
                    f=f
                    x+=1
            f=f
            if f+1==T2:
                return "IB"
            else:
                return "IB"
        else:
            c=0 #q
            v=0 #e
            while c<T1:
                if p1[c]==p2[c]:
                    v=v
                elif p1[c]!=p2[c]:
                    z=0 
                    while z<T1:
                       d=palabra2.find(p1[z])
                       if d==-1:
                           v+=1
                           z+=1
                       else:
                           v=v
                           z+=1
                c+=1
            if v==1:
                return "1S"
            elif v>1:
                return "+1"
            else:
                return "1S"

if __name__=="__main__":
    levenshtein("gato","gatito")
    levenshtein("hola","ola")
    levenshtein("gallina","gallina")
    levenshtein("caro","cara")

