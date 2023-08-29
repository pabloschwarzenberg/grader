# completa el código de la función
def suma_divisores(a):
    b = []
    f = []
    for i in range(1,a):
        if a%i == 0:
            b.append(i)
    for j in range(1,sum(b)+1):
        if sum(b)%j == 0:
            f.append(j)
    if sum(f) == 1:
        return (sum(b),True)
    else:
        return (sum(b),False)
