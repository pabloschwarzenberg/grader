# por favor escribe aquí tu función
def es_primo(numero):

  if numero > 1:

    x=0

    divisor=2

    while divisor<numero:

      resta = numero%divisor

      if resta==0:

        x+=1

      divisor+=1

    if x==0:

      return True

    else:

      return False

  else:

    return False



try:

  num_ingresado = int(input("Ingrese un numero: "))

  print(es_primo(num_ingresado))

except:

  print("Ingrese solo numeros porfavor")