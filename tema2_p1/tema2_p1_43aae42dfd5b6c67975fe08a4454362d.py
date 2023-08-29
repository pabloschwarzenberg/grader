def es_primo(n):
  if n==1:
    return False
  divisor=n-1
  
  while divisor>1:
   if n%divisor==0:
      return False
  
   divisor-=1
  return True 