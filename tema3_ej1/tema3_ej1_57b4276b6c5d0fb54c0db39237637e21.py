# completa el código de la función
def suma_divisores(a):
  suma = 0
  i = 1
  while i < a:
    if a%i == 0:
      suma += i
    i+=1

  if suma == 1:
    return (suma, True)
  return (suma, False)
           