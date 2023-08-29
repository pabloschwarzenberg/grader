# completa el código de la función
def amigos(da, niel):
    divisoresda = []
    for i in range(1, da):
        if da%i == 0:
            i = divisoresda.append(i)
    divisoresniel = []
    for i in range(1, niel):
        if niel%i == 0:
            i = divisoresniel.append(i)

    print("divisoresda =", divisoresda, "\n"+"divisoresniel =", divisoresniel)
    
    divisorda = 0
    for divisor in divisoresda:
        divisorda = divisorda + divisor
    print(divisorda)

    divisorniel = 0
    for divisor in divisoresniel:
        divisorniel = divisorniel + divisor
    print(divisorniel)

    if divisorniel == da and divisorda == niel:
        return True
    else:
        return False