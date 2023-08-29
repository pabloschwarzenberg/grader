import random

listaPalabras=['amor', 'boda', 'adivinanza', 'amarillo', 'silla','telefono', 'ballena', 'radio', 'automovil']

def seleccionRandom(listaPalabras):
    return random.choice(listaPalabras) #escojo palabra random de la lista


seleccionRandom(listaPalabras)

palabraEscogida = [] #creo lista
palabraEscogida.append(seleccionRandom(listaPalabras)) #guardo la palabra random en la lista
print(palabraEscogida) #imprimo la palabra random en la lista

print("comienza el juego! Se eligio una palabra al azar y tendras que adivinar la misma, introduce las letras que creas que tenga, tienes 5 intentos para adivinar la letra, si fallas quedas descalificado ")
letra=input("introduce una letra para saber si esta dentro de la palabra: ")



def verificacionLetra(letra):
  contador = 0

  while letra in palabraEscogida[0]:
    contador=contador+1
    print(f' la letra, {letra}, esta y has ganado, {contador}, punto')
    letra=input("introduce otra letra para saber si esta dentro de la palabra: ")
    print(palabraEscogida)


  else:
    contador=contador-1
    print(f'la letra, {letra}, no esta y tienes puntos, {contador}')
    letra=input("introduce otra letra para saber si esta dentro de la palabra: ")
    print(palabraEscogida)

verificacionLetra(letra)