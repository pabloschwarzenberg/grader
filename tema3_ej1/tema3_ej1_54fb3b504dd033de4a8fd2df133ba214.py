# completa el código de la función
def suma_divisores(a):
    div=[i for i in range(1,a) if a%i==0]
    var=sum(div)
    if var==1:
        return var,True
    return var,False
           