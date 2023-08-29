#Factores Primos
numero = int(input("ingrese numero "))

for i in range (2, numero + 1):
    while numero % i == 0:
      print(i)
      numero = numero / i