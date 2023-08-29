# completa el código de la función
def suma_divisores(a):
  l = []
  for i in range(1,a + 1):
    x = a % i
    if x == 0:
      l.append(i)
  l.remove(a)
  x = sum(l)
  if x == 1:
      t = True
  else:
      t = False
  return (x,t)

  
           