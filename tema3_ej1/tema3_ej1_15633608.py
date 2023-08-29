# completa el código de la función
def suma_divisores(a):
  suma = 0
  e = 1
  while e<a:
     if a%e==0:
       suma = suma + e
     e=e+1
  if suma == 1:
    b = True
  else:
    b = False
  return suma,b
a=1
while a<23:
  print(suma_divisores(a))
  a = a+1