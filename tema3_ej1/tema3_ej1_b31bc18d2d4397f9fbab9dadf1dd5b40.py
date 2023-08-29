# completa el código de la función
def sum_divisores(n):
  suma = 0
  divisor = n
  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        sum += divisor
  # Devuelve la suma de todos los divisores de n, sin incluir n
  return sum
print(suma_divisor(0))

print(suma_divisores(3)) # Debe ser sum de 1
# 1
print(suma_divisores(36)) # Debe ser sum de 1+2+3+4+6+9+12+18
# 55
print(suma_divisores(102)) # Debe ser be sum de 2+3+6+17+34+51
# 114