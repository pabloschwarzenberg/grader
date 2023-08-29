import random
inr= 0
num = random.randint(1, 20)
est = int (input("Ingrese un numero entero del 1 al 20:"))
while inr <= 5:
  inr = inr + 1
  if est < num:
    print("Mi numero es mayor") 
  if est> num:
    print("Mi numero es menor")
  if est == num:
    break
if est == num:
  print("Adivinaste, mi número era: ", num)
if est != num:
  print("No adivinaste, mi número era", num)
      