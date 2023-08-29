def suma_divisores(a):
    if a==1:
        return (0, False)
    divisores = [1]
    primo=True
    for i in range(2, a):
            if a % i == 0:
                divisores.append(i)
                z=sum(divisores)
                if z != 1:
                    primo=False
    return (sum(divisores), primo)