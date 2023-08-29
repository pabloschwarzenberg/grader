# completa el código de la función
def amigos(a,b):
  a_d = []
  b_d = []
  for i in range(1,a-1):
    if a % i == 0 :
      a_d.append(i)
  for i in range(1,b-1):
    if b % i == 0 :
      b_d.append(i)
  if sum(a_d) == b and sum(b_d) == a:
    return True
  else:
    return False
      
    
           