import random

num=random.randint(1,20)
intento = 0
ganaste = False

while intento < 5 and not ganaste:
  numero=int(input("intento "+str(intento + 1)+": "))
  if numero > num:
    print("mi número es menor")
  elif numero < num:
    print("mi número es mayor")
  else:
    print("Adivinaste, mi número era ", num);
    ganaste = True
  numero = numero + 1
  intento = intento + 1

if not ganaste:
  print("No adivinaste, mi número era ", num);
