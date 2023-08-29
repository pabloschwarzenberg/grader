def suma_divisores(a):
    suma=0
    estado=0
    for n in range(1,a):
        if a%n==0:
            m=n
            suma += m
    if suma==1:
        estado=True
    else:
        estado=False
    return (suma,estado)



