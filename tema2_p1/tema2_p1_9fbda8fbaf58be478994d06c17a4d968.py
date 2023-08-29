# por favor escribe aquí tu función
def es_primo(numero):

  if numero >1:

    a=0

    Numero_divisor=2

    while Numero_divisor<numero:

      resto = numero%Numero_divisor

      if resto==0:

        a+=1

      Numero_divisor+=1

    if a==0:

      return True

    else:

      return False

  else:

    return False



try:

  NN = int(input("Ingrese número: "))

  print(es_primo(NN))

except:

  print("Porfavor, ingrese solo numeros")
