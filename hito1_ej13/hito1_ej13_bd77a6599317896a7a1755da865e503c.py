#Factores Primos
x = int(2)
numero = int(input("> favor ingresar el numero a calular factores primos: "));
while(numero !=1):
    if(numero % x== 0):
        print(str(x)+ " ");
        numero = numero / x;
    else:
        x = x + 1;
              