# completa el código de la función
def amigos(a,b):
    LNumDivisoresA=[]
    LNumDivisoresB=[]
    for i in range(1,a):
        if a%i==0:
            LNumDivisoresA.append(i)
    for i in range(1,b):
        if b%i==0:
            LNumDivisoresB.append(i)
    sumaDivisoresA=0
    sumaDivisoresB=0
    for x in LNumDivisoresA:
        sumaDivisoresA+=x
    for x in LNumDivisoresB:
        sumaDivisoresB+=x
    if sumaDivisoresA == b and sumaDivisoresB == a:
       return True
    else:
        return False
