# Definir una función que recibe un número
def es_primo(numero):
  # Si el número es menor que 2, no es primo
  if numero < 2:
    return False
  # Si el número es 2, es primo
  if numero == 2:
    return True
  # Si el número es par, no es primo
  if numero % 2 == 0:
    return False
  # Recorrer los posibles divisores impares desde 3 hasta la raíz cuadrada del número
  for divisor in range(3, int(numero ** 0.5) + 1, 2):
    # Si el número es divisible por alguno de ellos, no es primo
    if numero % divisor == 0:
      return False
  # Si no se encontró ningún divisor, el número es primo
  return True
