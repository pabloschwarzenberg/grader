def suma_divisores(a):
    if a==1:
        return(0,False)
    else:
        i=1
        lista=[]
        while i<a:
            b=a/i
            b_int=int(b)
            if b==b_int:
                lista.append(i)
                i=i+1
            else:
                i=i+1
                continue
        suma=sum(lista)
        if suma==1 or suma==0:
           return (suma,True) 
        else:
            return (suma,False)
    
    