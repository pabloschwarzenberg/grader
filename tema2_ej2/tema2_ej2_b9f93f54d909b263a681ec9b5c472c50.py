def amigos(c,b):

  div_de_numero_1=1

  div_de_numero_2=1

  suma_div_numero_1=0

  suma_div_numero_2=0

  while div_de_numero_1<c:

    if c%div_de_numero_1==0:

      suma_div_numero_1+=div_de_numero_1

      print("divisor de %d es: %d" % (c,div_de_numero_1),"la suma de sus divisores de %d es: %d" %(c,suma_div_numero_1))

    div_de_numero_1+=1

  while div_de_numero_2<b:

    if b%div_de_numero_2==0:

      suma_div_numero_2+=div_de_numero_2

      print("divisor de %d es: %d" % (b,div_de_numero_2),"la suma de sus divisores de %d es: %d" %(b,suma_div_numero_2))

    div_de_numero_2 += 1

  if suma_div_numero_1==b and suma_div_numero_2==c:

    return True

  else:

    return False

try:

 numero_1 = int(input("Número 1: "))

 numero_2 = int(input("Número 2: "))

 print(amigos(numero_1,numero_2))

except:

 print("Por favor Ingrese un Número: ")