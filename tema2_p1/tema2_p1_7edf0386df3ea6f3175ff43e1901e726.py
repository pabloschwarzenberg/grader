# por favor escribe aquí tu función
def es_primo(Number):
  return
def es_primo(Number):

  if Number >1:

    Z=0

    divisor=2

    while divisor<Number:

      resto = Number%divisor

      if resto==0:

        Z+=1

      divisor+=1

    if Z==0:

      return True

    else:

      return False

  else:

    return False



try:

  Number_ingreso = int(input("Ingrese el numero: "))

  print(es_primo(Number_ingreso))

except:

  print("Ingrese sólo un número: ")
           