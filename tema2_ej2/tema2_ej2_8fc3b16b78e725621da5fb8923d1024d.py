# completa el código de la función
def amigos(a,b):

  divnumero1=1

  divnumero2=1

  sumadivnumero1=0

  sumadivnumero2=0

  while divnumero1<a:

    if a%divnumero1==0:

      sumadivnumero1+=divnumero1

      print("el divisor de %d es: %d" % (a,divnumero1),"la suma de divisores de %d es: %d" %(a,sumadivnumero1))

    divnumero1+=1

  while divnumero2<b:

    if b%divnumero2==0:

      sumadivnumero2+=divnumero2

      print("el divisor de %d es: %d" % (b,divnumero2),"la suma de divisores de %d es: %d" %(b,sumadivnumero2))

    divnumero2 += 1

  if sumadivnumero1==b and sumadivnumero2==a:

    return True

  else:

    return False

try:

 numero1 = int(input("Numero 1: "))

 numero2 = int(input("Numero 2: "))

 print(amigos(numero1,numero2))

except:

 print("Ingrese su numero")
           