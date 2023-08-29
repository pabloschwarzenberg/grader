# completa el código de la función
def suma_divisores(a):

    div=[i for i in range(1,a) if a%i==0]
    y=sum(div)
    if y==1:
        return y,True
    return y,False
           