# completa el código de la función
def amigos(a,b):
  divA = [1]
  divB = [1]
  for i in range (2, a):
      if a % i == 0:
          divA.append(i)
  for i in range (2, b):
      if b % i == 0:
          divB.append(i)
  if divA == [1] or divB == [1]:
      return False
  elif sum(divA) == b and sum(divB) == a:
      return True
  else:
      return False