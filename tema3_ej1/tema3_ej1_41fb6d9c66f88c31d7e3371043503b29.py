# completa el código de la función
def suma_divisores(a):
    divisores = 0
    for n in range(1, a):
        if a % n == 0:
            divisores = divisores + n

    if divisores == 1:
        return divisores, True
    else:
        return divisores, False


  
           