# completa el código de la función
def suma_divisores(n):
    a = []
    suma = 0
    for divisor in range(1, n):
        if (n % divisor) == 0 :
            a.append(divisor)
    for num in a :
        suma += num
    if suma < 1 :
        return suma, False
    if suma == 1 :
        return suma, True
    for i in range(2,suma):
        if suma % i == 0 :
            return suma, True
    return suma, False           