def amigos(a,b):

  divdenumero1=1

  divdenumero2=1

  sumadivnumero1=0

  sumadivnumero2=0

  while divdenumero1<a:

    if a%divdenumero1==0:

      sumadivnumero1+=divdenumero1

      print("divisor de %d es: %d" % (a,divdenumero1),"la suma de divisores de %d es: %d" %(a,sumadivnumero1))

    divdenumero1+=1

  while divdenumero2<b:

    if b%divdenumero2==0:

      sumadivnumero2+=divdenumero2

      print("divisor de %d es: %d" % (b,divdenumero2),"la suma de divisores de %d es: %d" %(b,sumadivnumero2))

    divdenumero2 += 1

  if sumadivnumero1==b and sumadivnumero2==a:

    return True

  else:

    return False

try:

 numero1 = int(input("Número 1: "))

 numero2 = int(input("Número 2: "))

 print(amigos(numero1,numero2))

except:

 print("Por favor Ingrese un Número")

           