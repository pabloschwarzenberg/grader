def es_primo(a):
  c=0
  for i in range(1,a+1):
    if a%i==0:
      c=c+1
  if c==2:
    return (True)
  else:
    return (False)
    