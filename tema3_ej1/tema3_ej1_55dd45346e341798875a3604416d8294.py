# completa el código de la función
def suma_divisores(a):
  div = list()
  sum = 0
  val = True
  for i in range(1,a):
    if a % i == 0:
      div.append(i)
  for i in div:
    sum += i
  if sum != 1:
    val = False
  return sum, val
