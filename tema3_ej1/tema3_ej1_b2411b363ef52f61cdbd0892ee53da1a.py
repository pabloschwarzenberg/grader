# completa el código de la función
def suma_divisores(a):
  l=[]
  for m in range(1,a-1):
      if a%m==0:
        l.append(m)
        b=sum(l)
      else:
        pass
  b=sum(l)
  if a==1:
    return (b,False)
  elif a==0:
    return (b,False)
  elif b==1:
    return (b,True)
  else:
    return (b,False)
           