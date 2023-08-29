def suma_divisores(a):
    divisores = [0]

    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
    x = sum(divisores)
    if x==1:
        return(x,True)
    else:
        return(x,False)
e=suma_divisores(7)
print(e)