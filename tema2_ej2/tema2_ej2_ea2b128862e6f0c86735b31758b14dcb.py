# completa el código de la funció
def amigos(a,b):
  divn1=1
  divn2=1
  sumdivn1=0
  sumdivn2=0

  while (divn1<a):

    if (a % divn1==0):
      sumdivn1 += divn1
    divn1 += 1

  while (divn2<b):

    if (b % divn2==0):
      sumdivn2 += divn2
    divn2 += 1

  if (sumdivn1==b and sumdivn2==a):
    return True

  else:
    return False

try:
 n1=int(input("Número 1: "))
 n2=int(input("Número 2: "))
 print(amigos(n1,n2))

except:
 print("---------ERROR----------")