# completa el código de la función
def amigos(a,b):
    divisoresA=[]
    sumaA=0
    divisoresB=[]
    sumaB=0
    for i in range(1, a + 1):
        if a % i == 0:
            divisoresA.append(i)
    for i in divisoresA:
        sumaA+=i
    for i in range(1, b + 1):
        if b % i == 0:
            divisoresB.append(i)
    for i in divisoresB:
        sumaB+=i
    if sumaA-a==b and sumaB-b==a:
        return True
    else:
        return False
           