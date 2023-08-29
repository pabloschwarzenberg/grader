def numero_perfecto(a):
    suma = 0
    for i in range(a):
        if i != 0:
            if a%i == 0:
                suma += i
    if suma == a:
        p =True
    else:
        p =False
    return(p)           