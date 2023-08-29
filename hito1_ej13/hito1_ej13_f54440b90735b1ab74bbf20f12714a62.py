#Factores Primos
num = int(input())
fact = []

lista_aux = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for a in lista_aux:
  if num % a == 0:
    fact.append(a)

for a in fact:
  print(a)