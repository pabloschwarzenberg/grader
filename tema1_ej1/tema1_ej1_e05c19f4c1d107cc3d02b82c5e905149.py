#Suma de los N primeros números
n = int(input())

suma = 0
for i in range(n + 1):
  suma += i
  
print(suma)