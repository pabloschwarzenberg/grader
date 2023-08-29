#Factores Primos
kk = int(2);
numero = eval(input("> Favor de ingresar el número a calcular factores primos: "));

while (numero != 1):

    if (numero % kk == 0):
        print(str(kk)+" ");
        numero = numero / kk;

    else:
        kk = kk + 1;