#Suma de los N primeros números
print("===============================")
print("Suma primeros números naturales")
print("===============================\n")

N = int(input("Inserte un número natural: "))

if N < 0:
  print("el valor ingresado no es un numero natural...")
  print("los numeros naturales son mayores al cero, intentelo de nuevo")
else:
  SN = (N * (N +1)) / 2
  print("La suma de los primeros números naturales de", N, "resulta en", SN)