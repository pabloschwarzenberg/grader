# completa el código de la función
def amigos(a,b):

  div_1=1

  div_2=1

  suma_1=0

  suma_2=0

  while div_1<a:

    if a%div_1==0:

      suma_1+=div_1


    div_1+=1

  while div_2<b:

    if b%div_2==0:

      suma_2+=div_2

    div_2 += 1

  if suma_1==b and suma_2==a:

    return True

  else:

    return False

try:

 N1 = int(input("Numero 1: "))

 N2 = int(input("Numero 2: "))

 print(amigos(N1,N2))

except:

 print("Ingrese un Numero: ")
