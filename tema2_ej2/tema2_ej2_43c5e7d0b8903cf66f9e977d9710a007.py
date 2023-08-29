# completa el código de la función
def amigos(a,b):
  if a!=b:
   sumaUno=0
   for i in (range(1, a + 1)):
    if a%i==0:
     sumaUno+=i
   sumaDos=0
   for i in range(1, b + 1):
    if b%i==0:
     sumaDos +=i
     
   if sumaDos-b == a and sumaUno-a == b:
    return True
  return False
