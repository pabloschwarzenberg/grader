import time
proponedor=input("cual es tu nombre ")
adivinador=input("cual es el nombre del contrincante?")
print("hola "+proponedor+ " y "+adivinador+" iniciemos el juego!")
print("")
time.sleep(1)
print("comenzar a jugar")
time.sleep(1)
palabra='prueba'
tupalabra=""
intentos=input("cuantas intentos desea tener en el juego? ")
input(intentos)
print("muy buena elección has escogido "+intentos+" intentos")

while intentos <0:
  fallas=0
  for letra in palabra:
    if letra in tupalabra:
      print(letra, end="")
    else:
      print("*", end="")
      fallas+=1
  if fallas==0:
    print("feliciades has ganado")
    break

  tuletra=input("introduce una letra: ")
  tupalbra+=tuletra

  if tuletra not in palabra:
    intentos-=1
    print("estas equivocado")
    print("tu tienes "+intentos+ "intentos")

else:
  print("gracias por participar")
