x = int(2);
numero = int(input("> Favor de ingresar el número a calcular factores primos: "));

while (numero != 1):

    if (numero % x == 0):
        print(str(x)+" ");
        numero = numero / x;

    else:
        x = x + 1;
def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    
    ##sumar divisores
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == 1:
        esPrimo = True
        return suma, esPrimo
    else:
        esPrimo = False
        return suma, esPrimo        