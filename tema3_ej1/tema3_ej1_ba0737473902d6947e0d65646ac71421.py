# completa el código de la función
def suma_divisores(a):
    dvsr=[]
    for i in range(1,a):
        if a%i==0:
            dvsr.append(i)
    b=0
    for i in range(0,len(dvsr)):
        b=b+dvsr[i]
    print(b)
    if a==1:
        d= False
    elif b==1:
        d= True
    else:
        d= False
    return b,d
