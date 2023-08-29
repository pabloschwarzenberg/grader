# completa el código de la función
def amigos(a,b):
    divA = []
    divB = []
    sumaA = 0
    sumaB = 0
    for i in range(1,a):
        if a % i == 0:
            divA.append(i)
    for i in range(1,b):
        if b % i == 0:
            divB.append(i)
    for i in divA:
        sumaA += i
    for i in divB:
        sumaB += i
    return sumaA == b and sumaB == a