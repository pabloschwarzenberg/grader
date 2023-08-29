#Suma de los N primeros números
continuar = True
suma = 0

while continuar:
  n = input("Introduzca valor de N: ")
  if n.isdigit():
    continuar = False
    suma = int(n) * (int(n) + 1)/2
  else:
    print("No es un valor válido. Intente nuevamente.")

print("La suma de los primeros números naturales de {} es {}".format(n, round(suma)))