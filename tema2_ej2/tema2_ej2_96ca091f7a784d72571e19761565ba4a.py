def amigos(a,b):
  sumaa=0
  sumab=0
  for i in range (1,a):
    if a%i==0:
      sumaa+=i
  for j in range (1,b):
    if b%j==0:
      sumab+=j
  if sumaa==b and sumab==a:
    return True
  else:
    return False