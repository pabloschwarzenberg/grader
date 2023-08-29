# completa el código de la función
def amigos(a,b):
  d1=1
  d2=1
  s1=0
  s2=0

  while d1<a:

    if a%d1==0:
      s1+=d1
      print("El divisor de %d: %d" % (a,d1),"la suma de los divisores de %d: %d" %(a,s1))

    d1+=1
  while d2<b:

    if b%d2==0:
      s2+=d2

      print("El divisor de %d: %d" % (b,d2),"la suma de los divisores de %d: %d" %(b,s2))
    d2 += 1

  if s1==b and s2==a:
    return True

  else:
    return False

try:
 n1 = int(input("Primero: "))
 n2 = int(input("Segundo: "))

 print(amigos(n1,n2))

except:

 print("Ingrese un número: ")