def amigos(a,b):
  listaA = []
  for i in range(1, a):
    divisorA = a % i
    if divisorA == 0:
      listaA.append(i)

  listaB = []
  for j in range(1,b):
    divisorB = b % j
    if divisorB == 0:
      listaB.append(j)

  sumaA = sum(listaA)

  sumaB = sum(listaB)

  if sumaA == b and sumaB == a:
    return True

  else:
    return False