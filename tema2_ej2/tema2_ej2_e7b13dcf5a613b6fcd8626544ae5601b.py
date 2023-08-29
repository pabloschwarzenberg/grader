# completa el código de la función
def amigos(a,b):
    divB = []
    divA = []
    for i in range(1,b):
        if b%i == 0:
            divB.append(i)
    for j in range(1,a):
        if a%j == 0:
            divA.append(j)
    sumA = sum(divA)
    sumB = sum(divB)
    if a == sumB and b == sumA:
        return True
    else:
        return False
        
           