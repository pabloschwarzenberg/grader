def amigos(a,b):
  div_1 = 1
  div_2 = 1
  suma_div1 = 0
  suma_div2 = 0

  while div_1<a:

    if a%div_1==0:
      suma_div1+=div_1
      ("divisor de %d es: %d" % (a,div_1),"la suma de divisores de %d es: %d" %(a,suma_div1))
    div_1+=1

  while div_2<b:
    if b%div_2==0:
      suma_div2+=div_2
      ("divisor de %d es: %d" % (b,div_2),"la suma de divisores de %d es: %d" %(b,suma_div2))
    div_2 += 1

  if suma_div1==b and suma_div2==a:
    return True

  else:
    return False

try:
 numero_1 = int(input("Número 1: "))
 numero_2 = int(input("Número 2: "))
 print(amigos(numero_1,numero_2))

except:
 print("Por favor Ingrese un Número")