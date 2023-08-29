#Factores Primos
numero = int(input('Ingrese su número: '))

f_primos = []
for i in range(2, numero + 1):
    while numero % i == 0:
        numero = numero / i
        f_primos.append(i)
for i in f_primos:
  print(i)