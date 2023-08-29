#Juego adivina mi número
import random
juegos=5
num=random.randint(1,20)
while juegos>0:
  n=int(input("n:"))
  if n>num:
    print("mi número es menor")
  elif n<num:
    print("mi número es mayor")
  else:
    print("adivinaste, mi número era",num)
  juegos=juegos-1
print("no adivinaste, mi número era",num) 