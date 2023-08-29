def suma_divisores(a):
    suma=0
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=1
            suma+=i
            print("Divisor: ",i)
    if suma==1:
        primo=True
    else:
        primo=False
    return (suma,primo)
