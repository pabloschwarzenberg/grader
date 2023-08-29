def es_primo(n):
  i=1
  c=0
  while n>=i:
    if n%i==0:
      c=c+1
    i=i+1
  if c==2:
    return True
  else:
    return False