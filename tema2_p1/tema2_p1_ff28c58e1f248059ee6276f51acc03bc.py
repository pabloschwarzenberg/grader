# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(numero):

  if numero >1:

    a=0

    d=2

    while d<numero:

      res = numero%d

      if res==0:

        a+=1

      d+=1

    if a==0:

      return True

    else:

      return False

  else:

    return False



try:

  numero1 = int(input("Ingrese número: "))

  print(es_primo(numero1))

except:

  print("Ingrese sólo número por favor")
