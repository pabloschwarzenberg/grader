# completa el código de la función
def suma_divisores(a):
    sumatoria=0
    for i in range(1, a):
        if a%i==0:
            sumatoria +=i
    if sumatoria==1:
        return (sumatoria, True)
    else:
        return (sumatoria, False)







