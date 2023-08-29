def amigos(a,b):
    d=0
    divisores=[]
    while d<a-1:
        d+=1
        if a%d==0:
           divisores.append(d)
    suma=sum(divisores)
    print(suma)
    if suma==b:
        d=0
        divisores2=[]
        while d<b-1:
            d+=1
            if b%d==0:
               divisores2.append(d)
        suma=sum(divisores2)
        if suma==a:
            return True
        else:
            return False
    else:
        return False