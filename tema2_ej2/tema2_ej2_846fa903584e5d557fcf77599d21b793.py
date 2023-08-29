def amigos(a,b):

  divnumero_1=1

  divnumero_2=1

  sumadivnumero_1=0

  sumadivnumero_2=0

  while divnumero_1<a:

    if a%divnumero_1==0:

      sumadivnumero_1+=divnumero_1

      

    divnumero_1+=1

  while divnumero_2<b:

    if b%divnumero_2==0:

      sumadivnumero_2+=divnumero_2

      

    divnumero_2 += 1

  if sumadivnumero_1==b and sumadivnumero_2==a:

    return True

  else:

    return False

try:

 numero_1 = int(input("Número 1: "))

 numero_2 = int(input("Número 2: "))

 print(amigos(numero_1,numero_2))

except:

 print("Por favor Ingrese un Número")