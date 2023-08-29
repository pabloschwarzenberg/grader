#Factores Primos Crea un programa que imprima la descomposición de factores primos de un número. Tu programa recibirá como entrada un número entero y debe imprimir cada factor primo del número en una línea separada. Por ejemplo para el número 22 debiera imprimir:2 11
x = int(2);
numero = int(input("> Favor de ingresar el número a calcular factores primos: "));

while (numero != 1):

    if (numero % x == 0):
        print(str(x)+" ");
        numero = numero / x;

    else:
        x = x + 1;    