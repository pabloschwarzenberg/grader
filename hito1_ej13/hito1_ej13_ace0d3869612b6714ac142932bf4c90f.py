#Factores Primos
numero=int(input("Ingrese Numero: "))
lisPrimos = []
for i in range(2,numero+1):
    while (numero % i == 0):
          lisPrimos.append(i)
          numero = numero / i
for fac in lisPrimos:
    print(fac)     