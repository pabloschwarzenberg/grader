def numero_perfecto(a):
    divisores = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            divisores.append(i)
            sumado = sum(divisores) - a
            if sumado == a:
                res = True
            else:
                res = False
                
    return res