#Factores Primos
x = int(2);
numero = int(input("Favor ingresar el número a calcular factores primos: "));
while (numero !=1):
       if (numero % x == 0):
            print(str(x) + "");
            numero = numero / x;
       else:
           x = x + 1;
     