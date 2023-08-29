#Adivina la palabra
from random import randint
      
def ocultar_letras(palabra, cantidad):

  palabra = "maquina"

  acumula = []

  palabra = list(palabra)

  while cantidad != 0:

    x = randint(1,len(palabra)-1)

    if x not in acumula:

     acumula.append(x)

     cantidad-=1

     palabra[x] = "_"

  palabra = "".join(palabra)

  return palabra



def revisar_letra(palabra_secreta,palabra,letra):

  x = list(palabra_secreta)

  palabra = list(palabra)

  if letra in x:

    y = palabra_secreta.find("-")

    palabra[y] = letra

  palabra = "".join(palabra)

  print(palabra)

  return palabra
#jerigonzo
def jerigonzo(string):
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido

         