# por favor escribe aquí tu función
def es_primo(x):

  if x >1:

    y=0

    d=2

    while d<x:

      r = x%d

      if r==0:

        y+=1

      d+=1

    if y==0:

      return True

    else:

      return False

  else:

    return False



try:

  N = int(input("Introduzca un numero: "))

  print(es_primo(N))

except:

  print("Introduzca un valor valido")