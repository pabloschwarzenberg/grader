# completa el código de la función
def amigos(a,b):
    divisoresA = [1]                                             
    for i in range(2,a+1):
        if a % i == 0:
            divisoresA.append(i)
    sumaA = sum(divisoresA)-a
    print(sumaA)

    divisoresB = [1]                                             
    for i in range(2,b+1):
        if b % i == 0:
            divisoresB.append(i)
    sumaB = sum(divisoresB)-b
    print(sumaB)
    
    if sumaA == b and sumaB == a:
        return True
    else:
        return False