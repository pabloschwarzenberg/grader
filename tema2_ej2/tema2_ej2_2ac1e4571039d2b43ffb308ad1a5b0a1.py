def amigos(a,b):

  divdenum_1=1
  divdenum_2=1
  sumdivnum_1=0
  sumdivnum_2=0

  while divdenum_1<a:
    if a%divdenum_1==0:

      sumdivnum_1+=divdenum_1

      print("divisor de %d es: %d" % (a,divdenum_1),"la suma de divisores de %d es: %d" %(a,sumdivnum_1))

    divdenum_1+=1

  while divdenum_2<b:

    if b%divdenum_2==0:

      sumdivnum_2+=divdenum_2

      print("divisor de %d es: %d" % (b,divdenum_2),"la suma de divisores de %d es: %d" %(b,sumdivnum_2))

    divdenum_2 += 1

  if sumdivnum_1==b and sumdivnum_2==a:

    return True

  else:

    return False

try:

 num1 = int(input("Número 1: "))
 num2 = int(input("Número 2: "))
 print(amigos(num1,num2))

except:
 print("Por favor Ingrese un Número")
