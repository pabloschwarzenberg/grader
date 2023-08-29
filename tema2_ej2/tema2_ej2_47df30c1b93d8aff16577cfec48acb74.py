# completa el código de la función
def amigos(a,b):
    divisoresA = [i for i in range(1, a + 1) if a % i == 0]
    divisoresB = [i for i in range(1,b+1)if b % i == 0]
    suma1 = sum(divisoresA) - a
    suma2 = sum(divisoresB) - b
    if (suma1 == b) and (suma2 == a):
        return True
    else:
        return False

