#Juego adivina mi número
import random
numero_random = random.randint(1,20)
n = 1

while n<=5:
  intento = int(input("Adivina número: "))

  if intento < numero_random:
    print("Mi número es mayor")

  elif intento>numero_random:
    print("Mi número es menor")

  else:
    print("Adivinaste, mi número era",numero_random )
    break

  if n == 5:
    print("No adivinaste, mi número era",numero_random )
  n += 1    