def numero_perfecto(a):
  l=[]
  for m in range(1,a-1):
      if a%m==0:
        l.append(m)
        b=sum(l)
      else:
        pass
  b=sum(l)
  if b==a:
    return True
  else:
    return False

           