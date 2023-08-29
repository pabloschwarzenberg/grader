# completa el código de la función
def divisores(num):
  div = []
  for i in range(1, num):
    if num % i == 0:
      div.append(i)
  return div
 

def amigos(a,b):
  div_a = divisores(a)
  div_b = divisores(b)
  if sum(div_a) == b and sum(div_b) == a:
    return True
  else:
    return False
           