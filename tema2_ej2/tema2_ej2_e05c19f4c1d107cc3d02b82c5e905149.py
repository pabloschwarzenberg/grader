# completa el código de la función
# completa el código de la función
def amigos(a,b):
  return suma_divisores(a) == b and a == suma_divisores(b)

def suma_divisores(n):
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i

  # print(sum)
  return sum
