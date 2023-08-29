def suma(numero):
    sumaDivisores = 0
    for j in range(1, numero):
        if numero % j == 0:
            sumaDivisores += j
    return sumaDivisores

def amigos(a,b):
    sumaA = suma(a)
    sumaB = suma(b)
    return sumaA == b and sumaB == a
n1 = 220
n2 = 284
if amigos(n1,n2):
    print("True")
else:
    print("False")