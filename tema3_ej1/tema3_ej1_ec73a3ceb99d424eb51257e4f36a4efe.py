def suma_divisores(n):
    divis = []
    for i in range(1, n):
        if n%i == 0:
            i = divis.append(i)
    
    ##sumar divisores
    sum = 0
    for divis in divis:
        sum = sum + divis
    if sum == 1:
        primo = True
        return sum, primo
    else:
        primo = False
        return sum, primo