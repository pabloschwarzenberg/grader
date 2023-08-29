def numero_perfecto(a):
  i=0
  lista=[]
  for x in range(1,a):
      if a%x==0:
          i=i+x
          lista.append(x)

  if i==a:
      return True

  else:
      return False