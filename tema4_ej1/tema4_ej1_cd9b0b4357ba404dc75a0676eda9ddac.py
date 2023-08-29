import random
words = "francia españa china japon italia chile rusia mexico alemania austria".split()
def obtenerPalabraAlAzar(listaDePalabras):





  indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)

  return listaDePalabras[indiceDePalabras]

 

def mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta):

  print([len(letrasIncorrectas)])

  print()

 

  print("Letras incorrectas:", end=" ")

  for letra in letrasIncorrectas:

    print(letra, end=" ")

  print()

 

  espaciosVacíos = "_" * len(palabraSecreta)

 

  for i in range(len(palabraSecreta)):



    if palabraSecreta[i] in letrasCorrectas:

      espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

 

  for letra in espaciosVacíos:



    print(letra, end=" ")

  print()

 

def obtenerIntento(letrasProbadas):




  while True:

    print("Adivina una letra.")

    intento = input(0)

    intento = intento.lower()

    if len(intento) != 1:

      print("Por favor, introduce una letra.")

    elif intento in letrasProbadas:

      print("Ya has probado esa letra. Elige otra.")

    elif intento not in "abcdefghijklmnñopqrstuvwxyz":

      print("Por favor ingresa una LETRA.")

    else:

      return intento

 

def jugarDeNuevo():




  print("¿Quieres jugar de nuevo? (sí o no)")

  return input().lower().startswith("s")

 

print("Ahorcado de paises.")
letrasIncorrectas = ""

letrasCorrectas = ""

palabraSecreta = obtenerPalabraAlAzar(words)

juegoTerminado = False

 

while True:

  mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)

 




  intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

 

  if intento in palabraSecreta:

    letrasCorrectas = letrasCorrectas + intento

 





    encontradoTodasLasLetras = True

    for i in range(len(palabraSecreta)):

      if palabraSecreta[i] not in letrasCorrectas:

        encontradoTodasLasLetras = False

        break

    if encontradoTodasLasLetras:

      print("¡Sí! ¡La palabra secreta es '" + palabraSecreta + "'! ¡Has ganado!")

      juegoTerminado = True

  else:

    letrasIncorrectas = letrasIncorrectas + intento

 




    if len(letrasIncorrectas) == 7:

      mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)

      print("¡Te has quedado sin intentos!\nDespués de " + str(len(letrasIncorrectas)) + " intentos fallidos y " + str(len(letrasCorrectas)) + " aciertos, la palabra era: '" + palabraSecreta + "'")

      juegoTerminado = True

 




  if juegoTerminado:

    if jugarDeNuevo():

      letrasIncorrectas = ""

      letrasCorrectas = ""

      juegoTerminado = False

      palabraSecreta = obtenerPalabraAlAzar(words)

    else:

      break