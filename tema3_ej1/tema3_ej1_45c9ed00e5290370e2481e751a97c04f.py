# completa el código de la función
def suma_divisores(n):
    divisores = []
    for i in range(1, n): 
        if n % i == 0:
            divisores.append(i)

    suma_de_los_divisores = sum(divisores)

    if suma_de_los_divisores == 1:
        primo = True
    else:
        primo = False

    return sum(divisores) , primo
           