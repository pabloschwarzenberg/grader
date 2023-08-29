import random
aleatorio = random.randint(1,20)
intento = 0
usuario = int(input("Adivina el número: "))
while intento < 4:
 if usuario < aleatorio:
  print("mi número es mayor")
  intento = intento + 1
 if usuario > aleatorio:
  print("mi número es menor")
  intento = intento + 1
 usuario = int(input("Adivina el número: "))
 if usuario == aleatorio:
  print("Adivinaste, mi número era",aleatorio)
  break
else:
  print("No adivinaste, mi número era",aleatorio)