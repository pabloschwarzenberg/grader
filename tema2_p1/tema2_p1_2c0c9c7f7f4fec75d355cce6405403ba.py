l=1000
n=2
numerosPrimos=[]
while n<=l:
  d=2
  primo=True
  while d<n:
    if n%d==0:
      primo=False
      break
    d=d+1
  if primo and n>1:
    numerosPrimos.append(n)
  n=n+1  
def es_primo(numero):
 if numero in numerosPrimos:   
  return True
 else:
  return False   