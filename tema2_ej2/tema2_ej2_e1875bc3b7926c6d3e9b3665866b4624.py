def amigos(a,b):
  SumaA=0
  SumaB=0 
  i=1
  e=1
  while (i<a):
      if(a%i==0):
          SumaA+=i
      i=i+1

  while (e<b):
      if(b%e==0):
          SumaB+=e
      e=e+1

  if SumaA==b and SumaB==a :
    return True

  else :
    return False