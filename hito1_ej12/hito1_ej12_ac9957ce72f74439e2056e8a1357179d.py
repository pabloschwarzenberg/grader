#Juego adivina mi número
import random
target = random.randint(1,20)
print(target)
error = 0
guess = 0
while guess != target:
  guess = int(input("Adivina el numero!: "))
  error += 1
  if guess == target:
    print("Adivinaste, mi número era {}".format(target))
    break
  if error == 5:
    print("No adivinaste, mi número era {}".format(target))
    break
  if guess != target:
    if guess > target:
      print("mi número es menor")
    elif guess < target:
      print("mi número es mayor")