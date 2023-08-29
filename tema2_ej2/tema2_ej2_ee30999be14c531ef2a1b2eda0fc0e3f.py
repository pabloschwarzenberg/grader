# completa el código de la función
def sumDiv(numero):
  suma=0
  for divisores in range(1,numero):
    if numero%divisores==0:
      suma+=divisores
  return suma
def amigos(a,b):
  sumaDivNum1=sumDiv(a)
  sumaDivNum2=sumDiv(b)
  if sumaDivNum1!=b or sumaDivNum2!=a:
    return False
  return True
           