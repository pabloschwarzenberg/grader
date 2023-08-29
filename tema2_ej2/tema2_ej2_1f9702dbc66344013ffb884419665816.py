def amigos(a,b):
  contador=1
  contador2=1
  divisoresa=[]
  divisoresb=[]
  sumadivisoresa=0
  sumadivisoresb=0
  while contador<a:
      if a%contador==0:
          divisoresa.append(contador)
      if b%contador==0:
          divisoresb.append(contador)
      contador+=1
  for i0 in divisoresa:
      sumadivisoresa=sumadivisoresa+i0
  for i1 in divisoresb:
      sumadivisoresb+=i1
  if sumadivisoresa==b and sumadivisoresb==a:
      return True
  else:
      return False
           