# completa el código de la función
def suma_divisores(a):
  lista = []
  for i in range(1,a):
    if a % i == 0:
      lista.append(i)
  if sum(lista) == 1:
    primo = True
  else:
    primo = False
  return sum(lista),primo