#Factores Primos
m = int(2);
numero = int(input("> Favor de ingresar el número a calcular factores primos: "));

while (numero != 1):

    if (numero % m == 0):
        print(str(m)+" ");
        numero = numero / m;

    else:
        m = m + 1;     