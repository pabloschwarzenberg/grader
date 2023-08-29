def amigos(a,b):

  division_1=1

  division_2=1

  suma_div_1=0

  suma_div_2=0

  while division_1<a:

    if a%division_1==0:

      suma_div_1+=division_1
      
    division_1+=1

  while division_2<b:

    if b%division_2==0:

      suma_div_2+=division_2

    division_2 += 1

  if suma_div_1==b and suma_div_2==a:

    return True

  else:

    return False

try:

 numero_1 = int(input("Número 1: "))

 numero_2 = int(input("Número 2: "))

 print(amigos(numero_1,numero_2))

except:

 print("Recuerda ingresar un Número")
           