def amigos(a,b):

  div_num_1=1

  div_num_2=1

  suma_div_num_1=0

  suma_div_num_2=0

  while div_num_1<a:

    if a%div_num_1==0:

      suma_div_num_1+=div_num_1

      print("El divisor de %d es: %d," % (a,div_num_1),"la suma de los divisores de %d es: %d" %(a,suma_div_num_1))

    div_num_1+=1

  while div_num_2<b:

    if b%div_num_2==0:

      suma_div_num_2+=div_num_2

      print("El divisor de %d es: %d," % (b,div_num_2),"la suma de los divisores de %d es: %d" %(b,suma_div_num_2))

    div_num_2 += 1

  if suma_div_num_1==b and suma_div_num_2==a:

    return True

  else:

    return False

try:

 num_1 = int(input("Ingrese el numero 1: "))

 num_2 = int(input("Ingrese el numero 2: "))

 print(amigos(num_1,num_2))

except:

 print("Ingrese un numero")