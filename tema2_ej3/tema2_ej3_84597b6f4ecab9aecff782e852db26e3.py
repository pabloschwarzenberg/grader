def numero_perfecto(a):
  n=0
  i=a-1
  while i > 0:
    pri=a%i
    if pri ==0:
      n+=i
    i-=1
  if n==a:
    return True
  else:
    return False

           