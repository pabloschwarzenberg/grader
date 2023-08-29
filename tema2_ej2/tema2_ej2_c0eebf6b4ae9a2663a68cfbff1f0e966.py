# completa el código de la función
def amigos(a,b):
    divisores = []
    for i in range(2, a):
        if a % i == 0:
            divisores.append(i)

    divisores2 = []
    for i in range(2, b):
        if b % i == 0:
            divisores2.append(i)

    if sum(divisores) == sum(divisores2):
        return False
    if sum(divisores) != sum(divisores2):
        return True
          