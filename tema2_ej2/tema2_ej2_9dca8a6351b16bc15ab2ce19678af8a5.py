# completa el código de la función
def amigos(a,b):
  divisoresA = []
  divisoresB = []
  sumaA=0
  sumaB=0
  for i in range(1,a):
    if a%i == 0:
      divisoresA.append(i)
  for j in range(1,b):
    if b%j == 0:
      divisoresB.append(j)
  for n in divisoresA:
    sumaA+=n
  for k in divisoresB:
    sumaB+=k
  if sumaA == b and sumaB == a:
    return True 
  return False
           