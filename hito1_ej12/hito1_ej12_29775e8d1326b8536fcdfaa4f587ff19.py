import random
secreto = random.randint(1, 20)
intentos = 5
print("Bienvenido al juego 'Adivina mi número'")
print("Tengo un número entre 1 y 20, y tendrás 5 intentos para adivinarlo.")
for i in range(1, intentos+1):
  print("Intento", i)
  guess = int(input("Ingresa tu número: "))
  if guess < secreto:
    print("Mi número es mayor.")
  elif guess > secreto:
  
    print("Mi número es menor.")
  else:
    print("Adivinaste, mi número era", secreto)
    break
if guess != secreto:
    print("No adivinaste, mi número era", secreto)