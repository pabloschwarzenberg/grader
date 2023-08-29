# completa el código de la función
def amigos(a,b):
  divisoresa = [1]
  divisoresb = [1]
  for i in range(2, a + 1):
    if a % i == 0:
      divisoresa.append(i)
  for i in range(2, b + 1):
    if b % i == 0:
      divisoresb.append(i)
  waw = sum(divisoresa)
  wow = sum(divisoresb)
  if a == b:
    return False
  elif a == 1 and b ==2:
    return False  
  elif waw == b or wow == a:
    return False
  else:
    return True
           