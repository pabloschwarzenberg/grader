def numero_perfecto(a):
    divisores = [1]
    for i in range(2,a):
        if a % i == 0:
            divisores.append(i)
    sD = sum(divisores)

    if sD == a:
        return True
    elif sD != a:
        return False
