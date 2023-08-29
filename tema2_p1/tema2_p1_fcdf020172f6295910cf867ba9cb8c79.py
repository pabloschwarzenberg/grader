# por favor escribe aquí tu función
def es_primo(numero):

  if numero > 1:

    x = 0

    divisor = 2

    while divisor < numero:

      resto = numero % divisor

      if resto == 0:

        x += 1

      divisor += 1

    if x == 0:

      return True

    else:

      return False

  else:

    return False



try:

  numero_ingreso = int(input("Ingrese numero: "))

  print(es_primo(numero_ingreso))

except:

  print("Ingrese sólo numero")          