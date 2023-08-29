def numero_perfecto(a):
    daivisores = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            daivisores.append(i)
            sumado = sum(daivisores) - a
            if sumado == a:
                res = True
            else:
                res = False
                
    return res
           