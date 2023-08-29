def suma_divisores(a):
    divisores = [1]

    for i in range(2, a ):
        if a % i == 0:
            divisores.append(i)
    return sum(divisores)



def numero_perfecto(a):
    if suma_divisores(a) == a:
        return True
    else:
        return False




