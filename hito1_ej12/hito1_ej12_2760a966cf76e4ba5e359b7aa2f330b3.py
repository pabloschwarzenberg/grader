#Juego adivina mi número
import random
c = 0
n = random.randint(1,20)
while c < 5:
      k = int(input("Ingrese número entre el 1 y el 20: "))
      if k < n:
          print("Mi número es mayor que el tuyo")
      elif k > n:
          print("Mi número es menor que el tuyo")
      elif k == n:
          print("Adivinaste, mi número era", str(n))
          break
      c += 1
if c >= 5 and k != n:
      print("No adivinaste, mi número era", str(n))
if c == 5 and k == n:
      print("Adivinaste, mi número era", str(n))