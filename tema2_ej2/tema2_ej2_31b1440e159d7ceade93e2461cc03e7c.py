# completa el código de la función
def amigos(a,b):
  lista_a = []
  lista_b = []

  for i in range(1,a):
    if a % i == 0:
      lista_a.append(i)
  x = sum(lista_a)

  for j in range(1,b):
    if b % j == 0:
      lista_b.append(j)
  y = sum(lista_b)

  if x == b and y == a:
    return(True)
  else:
    return(False)



