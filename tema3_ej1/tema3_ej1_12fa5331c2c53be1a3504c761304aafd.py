# completa el código de la función
def suma_divisores(a):
  global l1
  l1=[]
  global suma
  suma=0
  for i in range(1,a):
    if a%i==0:
      l1.append(i) 
  for i in l1:
    suma=suma+i
  if suma==1:
    esprimo=True
  else:
    esprimo=False
  return(suma,esprimo)
           