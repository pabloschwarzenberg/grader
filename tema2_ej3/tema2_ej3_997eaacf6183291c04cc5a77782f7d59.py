def numero_perfecto(a):
    acum = 0
    for i in range(1,a):
        if a%i == 0:
            acum += i
    if acum == a:
        return True
    else:
        return False
