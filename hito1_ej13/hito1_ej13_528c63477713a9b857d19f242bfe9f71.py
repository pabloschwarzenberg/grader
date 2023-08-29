def factoresprimos(n):
    factor=2
    f=[]
    while factor*factor<=n:
        if n%factor:
            factor+=1
        else:
            n//=factor
            f.append(factor)
    if n>1:
        f.append(n)
    return f
respuesta = int(input("ingresa el numero que desea sacar factores primos"))
r = factoresprimos(respuesta)
for factor in r:
    print(factor)