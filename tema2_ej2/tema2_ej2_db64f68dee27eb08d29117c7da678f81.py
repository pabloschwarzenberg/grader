def amigos(a,b):
  i=1
  q=1
  suma=0
  sumb=0
  while i<a:
      if a%i==0:
          suma=suma+i
      i=i+1
  while q<b:
      if b%q==0:
          sumb=sumb+q
          print(sumb)
      q=q+1
  if suma==b and sumb==a:
      return True
  else:
      return False
           