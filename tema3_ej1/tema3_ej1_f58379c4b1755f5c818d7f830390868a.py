# completa el código de la función
def suma_divisores(a):
  n = []
  m = []
  for i in range(1,a):
    if a % i == 0:
      n.append(i)
  for j in range(1, sum(n) + 1):
    if sum(n) % j == 0:
      m.append(j)
  if sum(m) == 1:
    return (sum(n), True)
  else:
   return (sum(n), False)