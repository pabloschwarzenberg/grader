#Factores Primos
#Entrada
x = int(2);
numero = int(input("Ingrese el número a descomponer un los N primos:"))

#Procesamiento 
while (numero != 1):
       if (numero % x == 0):
           print(str(x) + " ");
           numero = numero / x;
       else:
            x = x + 1;     