def amigos(a,b):

  numero_1=1

  numero_2=1

  suma_1=0

  suma_2=0

  while numero_1<a:

    if a%numero_1==0:

      suma_1+=numero_1

      print("divisor de %d es: %d" % (a,numero_1),"la suma de divisores de %d es: %d" %(a,suma_1))

    numero_1+=1

  while numero_2<b:

    if b%numero_2==0:

      suma_2+=numero_2

      print("divisor de %d es: %d" % (b,numero_2),"la suma de divisores de %d es: %d" %(b,suma_2))

    numero_2 += 1

  if suma_1==b and suma_2==a:

    return True

  else:

    return False

try:

 N_1 = int(input("Número 1: "))

 N_2 = int(input("Número 2: "))

 print(amigos(N_1,N_2))

except:

 print(" Ingreser el numero que usted disponga")
