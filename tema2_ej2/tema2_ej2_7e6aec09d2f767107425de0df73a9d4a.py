# completa el código de la función
def amigos(a,b):
  suma_ab= 0
  suma_ba= 0
  for i in range (1,a+1):
     if a%i==0:
         suma_ab += i
  for j in range (1,b+1):
     if b%j==0:
         suma_ba += j
  return suma_ab==suma_ba and a!= b
           