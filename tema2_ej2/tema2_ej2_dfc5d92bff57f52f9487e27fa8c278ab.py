# completa el código de la función
def amigos(a,b):
  divisores_1 = []
  divisores_2 = []
  for i in range(1,a):
    if (a % i == 0):
      divisores_1.append(i)
  for j in range(1,b):
    if (b % j == 0):
      divisores_2.append(j)
  if sum(divisores_1) == b and sum(divisores_2) == a:
    son_amigos = True
  else:
    son_amigos = False
  return son_amigos