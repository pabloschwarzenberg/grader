#Juego adivina mi número
import random
numerito = random.randint(2,19)
intento = 1
guess = 1

while intento < 5 and guess != numerito:
  guess = int(input("Adivina mi número >>> "))
  if guess > numerito:
    print("mi número es menor")
    intento += 1
  elif guess < numerito:
    print("mi número es mayor")
    intento += 1
  else:
    print("Adivinaste, mi númera era ",numerito)

if intento == 5:
  guess = int(input("Adivina mi número >>> "))
  if guess > numerito:
    print("No adivinaste, mi número era ",numerito)
    intento += 1
  elif guess < numerito:
    print("No adivinaste, mi número era ",numerito)
    intento += 1
  else:
    print("Adivinaste, mi númera era ",numerito)
    intento += 1