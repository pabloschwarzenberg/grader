# completa el código de la función
def suma_divisores(a):
    c=1
    d=0
    for i in range(a-1) :
        if a%c==0 :
            d=d+c
        c+=1
    if d==1 :       
        return  d, True
    else:
        return  d, False 