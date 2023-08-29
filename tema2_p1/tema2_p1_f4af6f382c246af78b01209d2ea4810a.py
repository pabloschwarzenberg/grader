# por favor escribe aquí tu función
def es_primo(numero):
  num = numero
  cantdiv = 0
  i = 1
  while i <= num:
    if num % i == 0:
      cantdiv = cantdiv + 1
    i = i + 1
  if cantdiv == 2:
    return True
  else:
    return False
           