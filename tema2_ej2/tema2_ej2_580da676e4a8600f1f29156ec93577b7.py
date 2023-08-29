# completa el código de la función
def numerosamigos(a,b):
  lisA = list(range(1,a))
  lisB = list(range(1,b))
  lista1=[]
  lista2=[]
  for x in lisA:
    if a % x == 0:
      lisA.append(x)
  for y in lisB:
    if b % y == 0:
      lisB.append(y)
  if sum(lisA)==b and sum(liaB)==a:
    return True
  return False
  
 a= eval(input('numero a: '))
 b= eval(input('numero b: '))
randint.amigos(a,b))
 