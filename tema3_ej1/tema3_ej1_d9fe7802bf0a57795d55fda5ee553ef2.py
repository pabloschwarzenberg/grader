# completa el código de la función
 
def suma_divisores(a):
    b = 1
    c = 0
    while b < a:
        if a % b == 0:
            c=c+b
        b=b+1
    if c==1:
        return (c,True)
    else:
        return (c,False)

           