# completa el código de la función
def suma_divisores(a):
    k=0
    for i in range(1,a):
        if a%i!=0:
            continue
        else:
            k+=i
    if k==1:
        return k,True
    else:
        return k,False
           