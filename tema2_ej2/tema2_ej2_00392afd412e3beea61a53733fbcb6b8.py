# completa el código de la función
def amigos(a,b):

  j1=1
  j2=1
  k1=0
  k2=0

  while j1<a:

    if (a%j1==0):

      k1+=j1

    j1+=1

  while j2<b:

    if (b%j2==0):

      k2+=j2

    j2 += 1

  if (k1==b) and (k2==a):

    return True

  else:

    return False

try:

 n1 = int(input("Número 1: "))
 n2 = int(input("Número 2: "))

 print(amigos(n1,n2))

except:

 print("Por favor Ingrese un Número")
           