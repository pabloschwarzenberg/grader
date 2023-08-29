# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(a):
        if i != 0:
            if a%i == 0:
                suma += i
    if suma == 1:
        p =True
    else:
        p =False
    return(suma,p)
           