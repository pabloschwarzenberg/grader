# completa el código de la función
def suma_divisores(a):
  suma = 0
  primo = False
  for i in range(1,a):
    if(a%i == 0):
      suma = suma +i
  if suma == 1:
    primo = True
  return (suma, primo)
           