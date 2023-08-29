#Juego adivina mi número
import random 
Random_num = random.randint(1,20)
print(Random_num)
x = 5

while x != 0:
  numero_elegido = eval(input())
  if numero_elegido == Random_num:
    x = 1
    print("Adivinaste, mi número era",Random_num )
  elif numero_elegido < Random_num and x > 1:
    print("mi número es mayor")
  elif numero_elegido > Random_num and x > 1:
    print("mi número es menor")
  x -= 1
  if x == 0 :
    print("No adivinaste, mi número era ",Random_num)      