import random
n = random.randint(1,20)
e=0
while True:
  x=int(input("ingrese un numero"))
  if x !=n:
    e+=1
    print(e)
    if x>n:
      print("mi numero es menor")
    else:
      print("mi numero es mayor")
  elif x==n:
    print("Adivinaste, mi numero era",n)
    break
  if e == 5:
    print("No adivinaste, mi numero era",n)
    break 