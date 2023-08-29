def es_primo(n):

  divisor=1
  c_div=0
  while divisor <= n:
    if n%divisor ==0:
       
       c_div = c_div + 1
    divisor = divisor +1
  if c_div==2:
     return True
  else:
       return False
       
entero=int(input())
lista=[]
for n in range(1,entero+1):

    if entero%n==0:
    
       lista.append(n)
       
for h in lista:
    if es_primo(h)==True:
      print(h)