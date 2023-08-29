                          #Suma de los N primeros números
n = int(input("ingrese un numnero "))
suma = n * (n+1)/2

while n <= 1:
  print(n)
  suma += 1
print(suma)