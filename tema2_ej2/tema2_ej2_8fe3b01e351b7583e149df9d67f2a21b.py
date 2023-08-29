# completa el código de la función
def amigos(a,b):

  div1=1

  div2=1

  sumadiv1=0

  sumadiv2=0

  while div1<a:

    if a%div1==0:

      sumadiv1+=div1   

    div1+=1

  while div2<b:

    if b%div2==0:

      sumadiv2+=div2

    div2 += 1

  if sumadiv1==b and sumadiv2==a:

    return True

  else:

    return False

try:

 n1 = int(input("Número 1: "))

 n2 = int(input("Número 2: "))

 print(amigos(n1,n2))

except:

 print("Por favor Ingrese un Número")

