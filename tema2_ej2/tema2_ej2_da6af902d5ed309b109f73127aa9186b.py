def amigos(a,b):
  suma1=0
  suma2=0
  for rango in range(1,a):
    if a%rango ==0:
      suma1+= rango
  for rangos in range(1,b):
    if b%rangos ==0:
      suma2+= rangos

  if suma2==a and suma1==b:
    return True
  else:
    return False