#Factores Primos
x = int(input("Ingrese numero: "))
valor = 2

while valor <= x:

  if x%valor == 0:
     print(valor)
     x = x / valor
  else:
    valor+= 1