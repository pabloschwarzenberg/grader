# Pedir al usuario que ingrese un número entero
numero = int(input())
# Definir una variable para guardar el factor primo actual
factor = 2
# Mientras el número sea mayor que 1
while numero > 1:
  # Si el número es divisible por el factor
  if numero % factor == 0:
    # Imprimir el factor
    print(factor)
    # Dividir el número por el factor
    numero //= factor
  else:
    # Incrementar el factor en 1
    factor += 1
