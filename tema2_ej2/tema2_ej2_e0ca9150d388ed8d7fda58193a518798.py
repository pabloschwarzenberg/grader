
def amigos(a, b):
    divisoresA = divisores(a)
    sumaDivisoresA = sumaDivisores(divisoresA)

    divisoresB = divisores(b)
    sumaDivisoresB = sumaDivisores(divisoresB)

    if(sumaDivisoresA == b and sumaDivisoresB == a):
        return True
    else:
        return False

def divisores(numero):
    divisores = []
    for i in range(2, int(numero/2)+1):
        if(numero%i == 0):
            divisores.append(i)
    divisores.append(1)
    return divisores

def sumaDivisores(divisores):
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    return suma
