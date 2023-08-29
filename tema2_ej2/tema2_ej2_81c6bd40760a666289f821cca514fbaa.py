# completa el código de la función
def amigos(a,b):

  div_val_1=1

  div_val_2=1

  suma_div_val_1=0

  suma_div_val_2=0

  while div_val_1<a:

    if a%div_val_1==0:

      suma_div_val_1+=div_val_1

      print("El divisor de %d es: %d," % (a,div_val_1),"La suma de los divisores de %d es: %d" %(a,suma_div_val_1))

    div_val_1+=1

  while div_val_2<b:

    if b%div_val_2==0:

      suma_div_val_2+=div_val_2

      print("El divisor de %d es: %d," % (b,div_val_2),"La suma de los divisores de %d es: %d" %(b,suma_div_val_2))

    div_val_2 += 1

  if suma_div_val_1==b and suma_div_val_2==a:

    return True

  else:

    return False

try:

 val_1 = int(input("Ingrese numero 1: "))

 val_2 = int(input("Ingrese numero 2: "))

 print(amigos(val_1,val_2))

except:

 print("Ingrese un numero")
           