def suma_divisores(x):
    divisores = [1]

    for i in range(2, x + 1):
        if (x % i == 0) and (i != x):
            divisores.append(i) 

    suma = sum(divisores)
    y = True
    for i in range(2, x):
        if x % i == 0:
            y = False
            break
            
    if x == 1:
        y = False
        suma = 0

    return (suma,y)