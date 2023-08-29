# completa el código de la función
#numeros amigos
def amigos(a,b):

  l1=1
  l2=1
  p1=0
  p2=0

  while l1<a:

    if (a%l1==0):

      p1+=l1

    l1+=1

  while l2<b:

    if (b%l2==0):

      p2+=l2

    l2 += 1

  if (p1==b) and (p2==a):

    return True

  else:

    return False

try:

 x1 = int(input("Número 1: "))
 x2 = int(input("Número 2: "))

 print(amigos(x1,x2))

except:

 print("Por favor Ingrese un Número")\
           