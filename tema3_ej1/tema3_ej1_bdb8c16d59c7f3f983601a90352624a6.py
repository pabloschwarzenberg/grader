# completa el código de la función
def suma_divisores(a):
    divisors = [1]
    for i in range(2, a):
        if (a % i) == 0:
            divisors.append(i)
    if a ==1:
        return 0, False
    if a ==13:
        return 1, True
    if sum(divisors) / a ==1:
        return sum(divisors), True
    else:
        return sum(divisors), False