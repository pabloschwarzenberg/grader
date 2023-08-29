#Suma de los N primeros números
print("Para sumar los n primeros números naturales...")
n = int(input("Ingrese los n números:"))
if n>=0:
  N = n*(n+1)/2
  print("La suma de los",n,"primeros números naturales es:",N)
if n<0:
  print("Opción fuera de rango")