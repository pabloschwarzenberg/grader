def numero_perfecto(a):
    divisores = []
    for n in range(1,a):
        if (a%n)==0:
            divisores.append(n)
    sum = 0
    for d in divisores:
        sum = sum + d
    if sum==a:
        perfecto = True
    else:
        perfecto = False
    return perfecto
           