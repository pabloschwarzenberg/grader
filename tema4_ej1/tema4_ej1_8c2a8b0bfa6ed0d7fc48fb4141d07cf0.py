from random import randint

def ocultarletras(palabra, cantidad):

  palabra = "maquina"

  acumula = []

  palabra = list(palabra)

  while cantidad != 0:

    x = randint(1,len(palabra)-1)

    if x not in acumula:

     acumula.append(x)

     cantidad-=1

     palabra[x] = ""

  palabra = "".join(palabra)

  return palabra
if __name__ == "__main__":
    pass
         