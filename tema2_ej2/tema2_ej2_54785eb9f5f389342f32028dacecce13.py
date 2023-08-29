# completa el código de la función
def amigos(a,b):
  listaA = []
  listaB = []
  for i in range(1,a):
    if a % i == 0:
      listaA.append(i)
  for j in range(1,b):
    if b % j == 0:
      listaB.append(j)
  if sum(listaA) == b and sum(listaB) == a:
    return True
  else:
    return False
