# completa el código de la función
def suma_divisores(a):
    divisores = [1]
    if a == 1:
       divisores = 0
       print(divisores)
       return False, divisores
    for i in range(2, a):
        if a % i == 0:
            divisores.append(i)
    if sum(divisores) == 1:
        return True, sum(divisores)
    if sum(divisores) != 1:
        return sum(divisores), False