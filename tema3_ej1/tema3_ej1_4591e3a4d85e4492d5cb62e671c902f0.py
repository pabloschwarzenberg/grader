# completa el código de la función
def suma_divisores(a):
    a=int(a)
    Suma_de_los_divisores = 0
    for i in range(1,a):
        if a%i==0:
            Suma_de_los_divisores+=i
    if a ==1:
        return (Suma_de_los_divisores, False)
    elif Suma_de_los_divisores==1:
        return (Suma_de_los_divisores, True)
    else:
        return (Suma_de_los_divisores, False)