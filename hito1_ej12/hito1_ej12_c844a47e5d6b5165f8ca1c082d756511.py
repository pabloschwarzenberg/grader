import random
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numero_programa=int(random.choice(lista))
intentos=5
numero_encontrado=False
while(intentos>0 and not numero_encontrado):
  numero_jugador=int(input("Ingresa un numero: "))
  if numero_jugador>numero_programa:
        print("Tu numero es mayor al mio")
        intentos=intentos - 1
  elif numero_jugador<numero_programa:
        print("Tu numero es menor al mio")
        intentos=intentos - 1
  else: 
        print("Adivinaste, mi numero era: ",numero_programa)
        numero_encontrado= True
