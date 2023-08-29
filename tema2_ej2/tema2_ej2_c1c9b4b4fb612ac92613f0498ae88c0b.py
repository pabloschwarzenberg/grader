def amigos(x,y):
  sumax=0
  sumay=0
  i=1
  while i<x:
    if x%i==0:
      sumax+=i
    i+=1
  i=1
  while i<y:
    if y%i==0:
      sumay+=i
    i+=1
  if sumax==y and sumay==x:
    return True
  else:
    return False