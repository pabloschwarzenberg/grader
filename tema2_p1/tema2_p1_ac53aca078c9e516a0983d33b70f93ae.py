# por favor escribe aquí tu función
def es_primo(numero):
  if numero > 1:
    x = 0
    divisor = 2

    while divisor < numero:

      n1 = numero % divisor

      if n1 == 0:

        x += 1

      divisor += 1

    if x == 0:

      return True

    else:

      return False

  else:

    return False



try:

  numingreso = int(input("Ingrese numero: "))

  print(es_primo(numingreso))

except:

  print("Ingrese sólo numero")              