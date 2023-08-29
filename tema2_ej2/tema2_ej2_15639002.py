# completa el código de la función
def amigos(a,b):
  suma=0
  h=0
  j=0
  for i in range(1,a):
    if (a%i==0):
      suma=suma+i
  suma2=0
  for i in range (1,b):
    if (b%i==0):
      suma2=suma2+i
  if a==suma2:
    if b==suma:
      h=b
    else:
      j=b
  return b==suma
    
    
  return
           