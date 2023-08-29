# completa el código de la función
def suma_divisores(a):
  global lista1
  global suma
  global esprimo
  lista1 = []
  suma = 0

  for i in range(1,a):
      if a%i==0:
          lista1.append(i)
  for i in lista1:
      suma=suma+i

  if suma==1:
      esprimo=True
  if suma !=1:
      esprimo=False
  
  return(suma,esprimo)
  if suma !=1:
      esprimo=False
  
  return(suma,esprimo)