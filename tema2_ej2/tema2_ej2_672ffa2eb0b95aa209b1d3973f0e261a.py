# completa el código de la función
def amigos(a,b):
    l=[]
    suma=0
    for i in a:
        for j in range(1,i):
            for k in b:
                if i%j==0:
                    suma+=k
                    l.append(i)
                    l.append(k)
    return l

           