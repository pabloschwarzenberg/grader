def amigos(a,b):
  l=[]
  m=[]
  for i in range(1, int(a)):
    if int(a)%i!=0:
      pass
    else:
      l.append(i)
  for i in range(1, int(b)):
    if int(b)%i!=0:
      pass
    else:
      m.append(i)
  if int(a)+int(b)==3:
    return False
  elif sum(l)==int(b) or sum(m)==int(a):
    return True
  else:
    return False