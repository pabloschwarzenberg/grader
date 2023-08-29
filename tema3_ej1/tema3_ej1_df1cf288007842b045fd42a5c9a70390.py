# completa el código de la función
def suma_divisores(a):
    sum = 0
    
    for i in range(1, a):
        if a % i == 0:
            sum += i

    if sum == 1:
        return sum, True
    
    else:
        return sum, False