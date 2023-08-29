#Factores Primos
num = input("Ingrese el Número: ")
num = int(num)
i = 2
prim = []

while i <= num:
    while num % i == 0:
      prim.append(i)
      num = int(num / i)
    i += 1
for x in prim:
  print(x)
