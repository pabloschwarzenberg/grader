import random



 

i=0
words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

 
def obtenerPalabraAlAzar(listaDePalabras):

  # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.



  indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)

  return listaDePalabras[indiceDePalabras]

 
  print('Letras incorrectas:', end=' ')

  for letra in letrasIncorrectas:

    print(letra, end=' ')

  print()

 

  espaciosVacíos = '_' * len(palabraSecreta)

 

  for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas



    if palabraSecreta[i] in letrasCorrectas:

      espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

 

  for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra



    print(letra, end=' ')

  print()

 

def obtenerIntento(letrasProbadas):
    if intento!=encontradoTodasLasLetras:
        i+=1
        return("ocupaste uno")

  # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.



while True:
    print('Adivina una letra.')
    intento = input()
    intento = intento.lower()
    if len(intento) != 1:
        print('Por favor, introduce una letra.')
    elif intento not in 'abcdefghijklmnñopqrstuvwxyz':

      print('Por favor ingresa una LETRA.')
      continue
    intento=input()

 

def jugarDeNuevo():

  # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.



  print('¿Quieres jugar de nuevo? (sí o no)')

  return input().lower().startswith('s')

 






letrasIncorrectas = ''

letrasCorrectas = ''

palabraSecreta = obtenerPalabraAlAzar(words)

juegoTerminado = False

  

  # Permite al jugador escribir una letra.



intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

 

if intento in palabraSecreta:

    letrasCorrectas = letrasCorrectas + intento

   

 

    # Verifica si el jugador ha ganado.



    encontradoTodasLasLetras = True

    for i in range(len(palabraSecreta)):

      if palabraSecreta[i] not in letrasCorrectas:

        encontradoTodasLasLetras = False

        break

    if encontradoTodasLasLetras:

      print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')

      juegoTerminado = True

else:

    letrasIncorrectas = letrasIncorrectas + intento

 

    # Comprobar si el jugador ha agotado sus intentos y ha perdido.



if i==7:
    print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
    juegoTerminado = True

 

  # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).



if juegoTerminado:

    if jugarDeNuevo():

      letrasIncorrectas = ''

      letrasCorrectas = ''

      juegoTerminado = False

      palabraSecreta = obtenerPalabraAlAzar(words)

    

