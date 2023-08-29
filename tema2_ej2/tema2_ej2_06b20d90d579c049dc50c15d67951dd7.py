# completa el código de la función
def amigos(a,b):
  divnum1 = 1
  divnum2 = 1
  sumdivnum1 = 0
  sumdivnum2 = 0
  while divnum1 < a:
    if a % divnum1 == 0:
      sumdivnum1 += divnum1
    divnum1 += 1
  while divnum2 < b:
    if b % divnum2 == 0:
      sumdivnum2 += divnum2
    divnum2 += 1
  if sumdivnum1 == b and sumdivnum2 == a:
    return True
  else:
    return False
  
  numero1 = int(input("Ingresa tu primer numero: "))
  numero2 = int(input("Ingresa tu segundo numero: "))
  print(amigos(numero1,numero2))