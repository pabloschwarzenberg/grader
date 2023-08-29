#Factores Primos
i = int(2);
numero = int(input("Ingrese el número ->"))
while (numero != 1):
       if (numero % i == 0):
           print(str(i) + " ");
           numero = numero / i;
       else:
            i = i + 1