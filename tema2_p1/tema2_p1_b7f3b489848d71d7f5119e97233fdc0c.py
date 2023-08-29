def es_primo(numerossss ):

  if numerossss >1:

    a=0

    divisor=2

    while divisor<numerossss :

      resto = numerossss %divisor

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

  numero_ingreso = int(input("Ingrese un número: "))

  print(es_primo(numero_ingreso))

except:

  print("Ingrese sólo número por favor")