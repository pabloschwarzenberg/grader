# completa el código de la función

def amigos(a,b):

  divis_de_numero_1=1

  divis_de_numero_2=1

  suma_divis_numero_1=0

  suma_divis_numero_2=0

  while divis_de_numero_1<a:

    if a%divis_de_numero_1==0:

      suma_divis_numero_1+=divis_de_numero_1

    divis_de_numero_1+=1

  while divis_de_numero_2<b:

    if b%divis_de_numero_2==0:

      suma_divis_numero_2+=divis_de_numero_2

    divis_de_numero_2 += 1

  if suma_divis_numero_1==b and suma_divis_numero_2==a:

    return True

  else:

    return False

try:

 numero_1 = int(input("Número 1: "))

 numero_2 = int(input("Número 2: "))

 print(amigos(numero_1,numero_2))

except:

 print("Por favor Ingrese un Número")