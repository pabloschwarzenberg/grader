# completa el código de la función
def amigos(a,b):
    divisoresA = []
    divisoresB = []
    for i in range(1,a+1):
        if a % i == 0:
            divisoresA.append(i)
    divisoresA.pop()
    for j in range(1,b+1):
        if b % j == 0:
            divisoresB.append(j)
    divisoresB.pop()
    if sum(divisoresA) == b and sum(divisoresB) == a:
        return True
    else:
        return False
     
        