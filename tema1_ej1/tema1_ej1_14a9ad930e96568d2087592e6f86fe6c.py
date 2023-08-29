#Suma de los N primeros números
N = int(input("Introduce un número N: "))
for n in range(1 , N + 1):
  n = n * (n + 1) / 2
  print(n)