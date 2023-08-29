# completa el código de la función
def obtenerSumaDivisores(numero):
    suma = 0
    for divisor in range(1,numero):
        resto = numero%divisor
        if resto == 0:
            print(str(resto))
            print("divisor " + str(divisor))
            suma += divisor #suma = suma + divisor
    return suma


def amigos(a,b):
    #6
    # 1, 2, 3
    sumaDivisoresA = obtenerSumaDivisores(a)
    sumaDivisresB = obtenerSumaDivisores(b)
    print(str(sumaDivisoresA))
    print(str(sumaDivisresB))
    if obtenerSumaDivisores(a) == b and obtenerSumaDivisores(b) == a:
        print("True")
        return True
    else:
        print("False")
        return False
amigos(220,284)
