# completa el código de la función
#numeros amigos
def amigos(a,b):
  div_a=1
  div_b=1
  
  for i in range(2,a):
      if a % i == 0:
           div_a=div_a+i
  for j in range(2,b):
      if b % i == 0:
           div_b=div_b+j
  if a==2 or b==2:
   if a==2:
      div_a=div_a+2
   if b==2:
      div_b=div_b+2
  if div_a==b or div_b==a:
     return(True)
  else:
     return(False)