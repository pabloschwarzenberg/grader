def numero_perfecto(n):
  sumatorio=0
  lista=[]
  for i in range(1,n):
    if n%i==0:
       sumatorio=sumatorio+i
       lista.append(i)
  if sumatorio==n:
    return True
  else:
    return False
      
           