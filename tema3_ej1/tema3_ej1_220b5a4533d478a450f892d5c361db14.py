def suma_divisores(y):
    L=[]
    x=0
    for i in range(1,y):
        if y%i==0:
            x=x+i
            L.append(i)
    if len(L)==1:
        i=True
    else:
        i=False
    return x,i