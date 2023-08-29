def es_primo(num):
 c=0
 for n in range(1,num+1):
  y=num%n
  if y==0:
   c=c + 1
 if c==2:
  return True
 else:
  return False 