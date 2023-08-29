# completa el código de la función
def suma_divisores(s):
    suma=0
    for r in range(1,s):
        if s%r==0:
            suma=suma+r
    if suma==1:
       return (suma, True)
    else:
       return (suma, False)
