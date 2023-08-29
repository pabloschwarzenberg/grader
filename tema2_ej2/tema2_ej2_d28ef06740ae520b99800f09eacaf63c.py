# completa el código de la función
def amigos(a,b):
  count = 0
  for i in range(a):
    if i == 0:
      continue
    elif a%i == 0:
      count+=i 
    else:
      continue
  count2 = 0    
  for i in range(b):
    if i == 0:
      continue
    elif b%i == 0:
      count2 += i
    else:
       continue
  if ((count == b) and (count2 == a)):
    return True
  else:
    return False
           