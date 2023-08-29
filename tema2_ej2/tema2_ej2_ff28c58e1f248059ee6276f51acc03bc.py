# completa el código de la función
def amigos(a,b):

  D1=1

  D2=1

  SD1=0

  SD2=0

  while D1<a:

    if a%D1==0:

      SD1+=D1

      

    D1+=1

  while D2<b:

    if b%D2==0:

      SD2+=D2

      

    D2 += 1

  if SD1==b and SD2==a:

    return True

  else:

    return False

try:

 numero_1 = int(input("Número 1: "))

 numero_2 = int(input("Número 2: "))

 print(amigos(numero_1,numero_2))

except:

 print("Por favor Ingrese un Número")
