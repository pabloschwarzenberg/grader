#Suma de los N primeros números
n = int(input('ingrese un numero natural')) 
N = 0
while N < n:
  num = int(n*(n + 1)/2)
  print(num)
  N += 1
  
  