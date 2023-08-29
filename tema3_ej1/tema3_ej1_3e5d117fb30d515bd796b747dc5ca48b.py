# completa el código de la función
def suma_divisores(a):
  suma = 0
  for num in range(1,a):
    if a % num == 0:
      suma += num
  if suma == 1:
    es_primo = True
  else:
    es_primo = False
  return (suma, es_primo)
           