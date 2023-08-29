def amigos(a,b):

  div_de_numeross_1=1

  div_de_numeross_2=1

  suma_div_numeross_1=0

  suma_div_numeross_2=0

  while div_de_numeross_1<a:

    if a%div_de_numeross_1==0:

      suma_div_numeross_1+=div_de_numeross_1

      

    div_de_numeross_1+=1

  while div_de_numeross_2<b:

    if b%div_de_numeross_2==0:

      suma_div_numeross_2+=div_de_numeross_2

      

    div_de_numeross_2 += 1

  if suma_div_numeross_1==b and suma_div_numeross_2==a:

    return True

  else:

    return False

try:

 numeros_1 = int(input("Número 1: "))

 numeros_2 = int(input("Número 2: "))
 print()



except:

 print("Por favor Ingrese un Número")
