def numero_perfecto(n):
    divisores = []
    for i in range(1, n): 
        if n % i == 0:
            divisores.append(i)

    suma_de_los_divisores = sum(divisores)

    if suma_de_los_divisores == n:
        num_perfecto = True
    else:
        num_perfecto = False

    return num_perfecto

