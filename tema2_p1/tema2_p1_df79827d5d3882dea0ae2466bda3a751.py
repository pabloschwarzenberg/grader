def es_primo(numero):
  if numero == 1:
    return False
  for n in range(2, numero):
    if numero % n == 0:
      print("No es primo", n, "es divisor")
      return False
  print("Es primo")
  return True
try:
  x = int(input("Ingresa un numero: "))
  print(es_primo(x))
except:
  print("Numero incorrecto")