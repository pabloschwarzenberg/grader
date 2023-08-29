# por favor escribe aquí tu función
def es_primo(numero):
  n = numero
  contador = 0
  for i in range(1,n+1):
    if n % i == 0:
      contador += 1
  if contador == 2:
    return True
  elif n == 1:
    return False
  else:
    return False
x = es_primo(24)
print(x)