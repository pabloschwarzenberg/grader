# completa el código de la función
def suma_divisores(a):
  listaA = []
  for i in range(1,a):
    if a % i == 0:
      listaA.append(i)
  if sum(listaA) == 1:
    primo = True
  else:
    primo = False
  return sum(listaA),primo
           