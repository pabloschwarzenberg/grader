import random
def Adivina_mi_numero():
  numero_secreto = random.randint(1, 20)
  intentos = 5
  
  print("Bienvenido a Adivina mi numero!")
  print("Tienes 5 intentos para adivinar el numero, esta entre el 1 y 20")
  print("tienes", intentos, "intentos")
  
  while intentos > 0:
    numero = int(input("Ingresa tu numero:"))
     
    if numero == numero_secreto:
      print("adivinaste, mi numero era", numero_secreto)
      return
    elif numero < numero_secreto:
      print("mi numero es mayor")
    else:
      print("mi numero es menor")

    intentos -= 1
  
  print("No adivinaste. Mi numero era", numero_secreto)
  
Adivina_mi_numero()