# Importar el módulo random para generar números aleatorios
import random
# Generar un número aleatorio entre 1 y 20 y guardarlo en una variable
numero_secreto = random.randint(1, 20)
# Definir una variable para controlar el número de intentos
intentos = 0
# Definir una variable para indicar si el jugador adivinó o no
adivino = False

# Mientras el número de intentos sea menor que 5 y el jugador no haya adivinado
while intentos < 5 and not adivino:
  # Pedir al jugador que ingrese un número
  numero = int(input("Ingresa un número entre 1 y 20: "))
  # Incrementar el número de intentos
  intentos += 1
  # Si el número ingresado es igual al número secreto
  if numero == numero_secreto:
    # Imprimir un mensaje de felicitación y el número secreto
    print("Adivinaste, mi número era", numero_secreto)
    # Cambiar la variable adivino a True para salir del ciclo
    adivino = True
  # Si el número ingresado es menor que el número secreto
  elif numero < numero_secreto:
    # Imprimir un mensaje indicando que el número secreto es mayor
    print("Mi número es mayor")
  # Si el número ingresado es mayor que el número secreto
  else:
    # Imprimir un mensaje indicando que el número secreto es menor
    print("Mi número es menor")

# Si el jugador no adivinó después de los 5 intentos
if not adivino:
  # Imprimir un mensaje de fracaso y el número secreto
  print("No adivinaste, mi número era", numero_secreto)
