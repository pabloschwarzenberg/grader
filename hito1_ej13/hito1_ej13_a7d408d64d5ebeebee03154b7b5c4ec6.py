def divisor(a):
    d=0
    divisores=[]
    while d<a-1:
        d+=1
        if a%d==0:
           divisores.append(d)
    return divisores
def es_primo(n):
  d=2
  primo=True
  while d<n:
    if n%d==0:
      primo=False
      break
    d+=1
  if primo and n>1:
    return True
  else:
    return False       
n=int(input())
if n==2:
    print ("2")
else:
  for e in divisor(n):
      if es_primo(e):
          print(e)