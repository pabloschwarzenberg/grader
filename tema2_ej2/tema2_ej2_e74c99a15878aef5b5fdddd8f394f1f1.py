def amigos(a,b):
  amigos=False
  def sd(n):
    i=1
    sd=0
    while i<n:
      if n%i==0:
        sd=sd+i
      i=i+1
    return sd
  if sd(a)==b and sd(b)==a:
    amigos=True
  return amigos