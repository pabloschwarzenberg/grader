# completa el código de la función
print("Hola estudiante")
def amigos(a,b):

  div_de_num_1=1

  div_de_num_2=1

  suma_div_num_1=0

  suma_div_num_2=0

  while div_de_num_1<a:

    if a%div_de_num_1==0:

      suma_div_num_1+=div_de_num_1

      print("divisor de %d es: %d" % (a,div_de_num_1),"la suma de divisores de %d es: %d" %(a,suma_div_num_1))

    div_de_num_1+=1

  while div_de_num_2<b:

    if b%div_de_num_2==0:

      suma_div_num_2+=div_de_num_2

      print("divisor de %d es: %d" % (b,div_de_num_2),"la suma de divisores de %d es: %d" %(b,suma_div_num_2))

    div_de_num_2 += 1

  if suma_div_num_1==b and suma_div_num_2==a:

    return True

  else:

    return False

try:

 num_1 = int(input("Ingresa tu primer numero: "))

 num_2 = int(input("Ingresa tu segundo numero: "))

 print(amigos(num_1,num_2))

except:

 print("Por favor Ingrese un Número")
           