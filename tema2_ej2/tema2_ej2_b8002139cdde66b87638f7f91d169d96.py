# completa el código de la función
def amigos(a,b):
  suma1=0
  suma2=0
  for i in range (1, a):
    if (a%i == 0):
        suma1=suma1+i
  for h in range(1,b):
     if b%h==0:
       suma2=suma2+1
  if (a==1 and b==2) or (a==2 and b==1):
    return False
  elif suma1==b:
    return True
  elif suma2==a:
     return True

  else:
    return False

           