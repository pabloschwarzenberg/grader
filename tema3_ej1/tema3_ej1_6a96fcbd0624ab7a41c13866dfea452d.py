# completa el código de la función
def suma_divisores(a):
  divisores = []
  i = 1
  while i < a:
    if a % i == 0:
      divisores.append(i)
    i = i + 1
  suma = sum(divisores)
  
  if a < 0:
    return (0, False)
  if suma == 1:
    return (suma, True)
  return (suma, False)
           