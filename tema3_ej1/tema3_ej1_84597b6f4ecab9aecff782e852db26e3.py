# completa el código de la función
def suma_divisores(a):
  n=0
  i=a-1
  while i > 0:
    pri=a%i
    if pri ==0:
      n+=i
    i-=1
  if n == 1:
    primo = True
  else:
    primo = False
  return n, primo

           