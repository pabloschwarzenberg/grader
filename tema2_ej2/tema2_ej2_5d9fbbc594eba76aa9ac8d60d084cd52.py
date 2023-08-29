# completa el código de la función
def amigos(a,b):
    divisoresA = []
    divisoresB = []
    n = 1
    while n <= a:
        modA = a%n
        if modA == 0:
            divisoresA.append(n)
        n+=1
    n = 1
    while n <= b:
        modB = b%n
        if modB == 0:
            divisoresB.append(n)
        n+=1
    sumA = 0
    for c in range(len(divisoresA)):
        sumA+=divisoresA[c]
    sumB = 0
    for d in range(len(divisoresB)):
        sumB+=divisoresB[d]
    if (sumA == sumB) and (a != b):
        return True
    else:
        return False
        