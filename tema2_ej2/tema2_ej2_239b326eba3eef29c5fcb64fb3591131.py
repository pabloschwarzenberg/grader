# completa el código de la función
def amigos(a,b):
  contador = 0
  if a == b:
    return False
  for i in range (1,a+1):
    if a % i == 0:
      contador += i
  print(contador)
  contador1 = 0
  for o in range (1,b+1):
    if b % o == 0:
      contador1 += o
  print(contador1)
  if contador == contador1:
    return True
  else:
    return False