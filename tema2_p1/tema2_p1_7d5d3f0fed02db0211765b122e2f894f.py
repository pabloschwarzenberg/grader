# por favor escribe aquí tu función
def es_primo(numero):
  num = numero
  i = 2
  if num == 1:
    return False
  while i < num:
      kik = num % i
      if kik == 0:
          return False
      i += 1
  return True
           