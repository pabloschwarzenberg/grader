def numero_perfecto(a):
    sumador = 0
    for i in range(1,a+1,1):
        if a%i == 0:
            sumador = sumador + i
    b = sumador - a
    if b == a:
        return True
    else:
        return False