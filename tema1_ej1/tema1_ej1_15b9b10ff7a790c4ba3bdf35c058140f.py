#Suma de los N primeros números
n = int(input("Ingrese un número: "))
if n > 0:
  calcular = n*(n + 1)/2
  print("La suma de los N primeros números naturales es: ", calcular)
else:
  print("No se puede determinar")
