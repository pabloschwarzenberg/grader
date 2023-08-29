def numero_perfecto(a):
    divisores = []
    for i in range(1, a):
        if a%i == 0:
            divisores.append(i)
    if sum(divisores) == a:
        return True
    else:
        return False





