#Factores Primos
n = int(2);
numero = int(input(" Ingrese el numero primo: "));
while(numero != 1):

  if (numero % n == 0):
    print(str(n) + " ");
    numero = numero / n;
  else:
      n = n + 1