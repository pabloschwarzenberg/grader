# completa el código de la función
def amigos(a,b):
    divisor = 1
    divisores = []
    while divisor < a:
        if a % divisor == 0:
            divisores.append(divisor)
        divisor += 1
    sumaDeElementos = sum(divisores)
    
    if sumaDeElementos == b:
        valor = True
    else:
        valor = False
    return valor
           