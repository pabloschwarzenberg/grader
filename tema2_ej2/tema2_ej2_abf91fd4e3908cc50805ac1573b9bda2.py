# completa el código de la función
def amigos(a,b):
   
  diva=a
  divb=b

  h=0
  k=0

  while 0 < diva:
      restoa=a%diva
      if restoa==0:
          h+=diva
      diva-=1

  while 0 < divb:
      restob=b%divb
      if restob==0:
          k+=divb
      divb-=1
  if a == b:
      return False
      
  if k == h:
      return True
      
  else:
      return False

           