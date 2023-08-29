def suma_divisores(a):
    d=[1]
    for i in range(2,a+1):
        if a%i == 0 and a!=i:
            d.append(i)
    suma=sum(d)
    primo=False
    if a == 1:
        suma=0
    if suma == 1:
        primo=True
    return (suma,primo)
