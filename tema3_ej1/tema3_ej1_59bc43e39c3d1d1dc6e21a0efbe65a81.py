def suma_divisores(a):
    l=[]
    num=0
    for x in range(1,a):
        if a%x==0:
            num=num+x
            l.append(x)
    if len(l)==1:
        x=True
    else:
        x=False
    return num,x