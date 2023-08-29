#Factores Primos
def imprimir_factores_primos(numero):
 # Comience con dos, que es el primer primo
factor = 2
    # Continúe hasta que el factor sea mayor que el número
while factor <= numero:
    # Verificar si el factor es un divisor de número
    if not (numero % factor != 0):
        # Si es así, imprímalo y divida el número original
    print(factor)
            numero /= factor
    else:
        # Si no es así, incremente el factor en uno
            factor += 1
    return "Done"