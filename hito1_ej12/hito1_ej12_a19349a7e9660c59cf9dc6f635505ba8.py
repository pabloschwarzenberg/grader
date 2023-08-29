import random
numero = random.randint(1,20)
print(numero)
intento = 0
numero_ingresado = int(input("Ingrese un numero: "))

while intento <= 5:

  if numero_ingresado == numero:
    print("Adivinaste, mi número era",numero)
    break

  elif intento == 5:
    print("No adivinaste, mi número era",numero)
    break

  elif numero_ingresado != numero:
    intento = intento + 1
    if numero_ingresado > numero:
      print("el número ingresado es menor que el número secreto")
    elif numero_ingresado < numero:
      print("el número ingresado es mayor que el número secreto")