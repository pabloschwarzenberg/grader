# completa el código de la función
def suma(a, b):
    for i in range(2, a):
        if a % 2 == 0:
            b = b + 1
    return b


def amigos(n1, n2):
    sum1, sum2 = 1, 1
    sum1 = suma(n1, sum1)
    sum2 = suma(n2, sum2)
    if (sum1 == n2) and (sum2 == n1):
        return True
    else:
        return False


x = int(input('Ingrese el primer numero: '))
y = int(input('Ingrese el segundo valor: '))

suma(amigos(x, y))
