#Suma de los N primeros números
n = int(input())
suma = 0 
N = 0

while N <= n :

  suma = n *(n + 1)/2
  N += 1
print(suma)