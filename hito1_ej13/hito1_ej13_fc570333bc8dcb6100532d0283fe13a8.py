#Factores Primos
numero = int(2);
x = int(input("> Ingresar  el numero a calcular factores primos"));

while (x != 1):

    if (x % numero == 0):
        print(str(numero)+"");
        x=x/numero;
        
    else:
        numero=numero+1;