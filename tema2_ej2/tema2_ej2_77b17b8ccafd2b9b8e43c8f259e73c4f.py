# completa el código de la función
def amigos(a,b):
  sum_a = 0
  sum_b = 0
  resultado = False
  for i in range(1, a):
    if(a % i == 0):
        sum_a += i
  for n in range(1, b):
    if(b % n == 0):
        sum_b += n
  if(sum_a == b and sum_b == a):
    resultado = True
  return resultado