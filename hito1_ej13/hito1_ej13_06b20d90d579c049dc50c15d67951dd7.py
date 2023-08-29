#Factores Primos
num = int(input("Ingrese Número: "))

ns = 2

while ns <= num:

  if num % ns == 0 :

    print(ns)

    num = num/ns

  else:

    ns += 1