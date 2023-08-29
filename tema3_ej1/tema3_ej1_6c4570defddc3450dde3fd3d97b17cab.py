# completa el código de la función
def suma_divisores(a):
    l_div = []
    for x in range(1, a):
        if a % x == 0:
            l_div.append(x)
    
    if sum(l_div) == 1:
        return sum(l_div),True
    else:
        return sum(l_div),False
