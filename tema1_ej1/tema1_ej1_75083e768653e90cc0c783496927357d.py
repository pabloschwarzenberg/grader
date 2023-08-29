#Suma de los N primeros números

n = int(input("Ingrese un numero Natural"))
if n >= 1:
  a = (n*(n+1))/2
  print(a)
else:
  print("Ingrese un numero Natural mayor a 1")