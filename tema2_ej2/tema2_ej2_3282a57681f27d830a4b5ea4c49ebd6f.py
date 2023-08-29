# completa el código de la función
def amiguis(numero1,numero2):
  count1=0
  count2=0
  for x in range(1,numero1):
    if numero1%x ==0:
      count1=count1+1
  for x in range(1,numero2):
    if numero2%x ==0:
      count2=count2+1
  if count1==count2:
     return True
  else:
     return False