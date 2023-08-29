# completa el código de la función
def amigos(x,y):
  suma_x=0
  suma_y=0
  for a in range(1,x):
      if x%a==0:
          suma_x+=a
  for b in range(1,y):
      if y%b==0:
          suma_y+=b
  if (suma_x == y) and (suma_y== x):
       return True
  else:
       return False
