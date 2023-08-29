# por favor escribe aquí tu función
def es_primo(Number):
  return
def es_primo(Number):

  if Number >1:

    a=0

    divisor=2

    while divisor<Number:

      resto = Number%divisor

      if resto==0:

        a+=1

      divisor+=1

    if a==0:

      return True

    else:

      return False

  else:

    return False



try:

  Number_ingreso = int(input("Adjunte un número: "))

  print(es_primo(Number_ingreso))

except:

  print("Adjunte sólo un número por favor")