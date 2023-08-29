# completa el código de la función
def amigos(a, b):
    A = divisores(a)
    print(A)
    B = divisores(b)
    print(B)
    if A == b and B == a:
        confirmacion = True
    else:
        confirmacion = False
    return confirmacion


def divisores(x):
    divisor = []
    for i in range(1, x):
        if x % i == 0:
            divisor.append(i)
    Suma = sum(divisor)
    return Suma

           