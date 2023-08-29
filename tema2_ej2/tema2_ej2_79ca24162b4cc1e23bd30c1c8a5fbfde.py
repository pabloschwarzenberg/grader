def amigos(a,b):
    suma=0
    sumatoria=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    for i in range(1,b):
        if b%i==0:
            sumatoria=sumatoria+i
    if sumatoria==a and suma==b:
        return True
    else:
        return False