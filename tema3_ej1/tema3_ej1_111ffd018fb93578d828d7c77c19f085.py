# completa el código de la función
def suma_divisores(a):
    list=[]
    x=0
    for y in range(1,a):
        if a%y==0:
            x=x+y
            list.append(y)
    if len(list)==1:
        y=True
    else:
        y=False
    return x,y