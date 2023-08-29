import random
a = random.randint(1,20)
b = int(input("Ingresa un número:"))
intentos = 5
if a==b:
    print("Adivinaste, mi número era ",a)
else:
  while a != b and intentos>0:
    if b<a:
      print("mi número es mayor")
    if b>a:
      print("mi número es menor")
    b = int(input("Ingresa un número:"))
    if a==b:
      print("Adivinaste, mi número era ",a)
    intentos-=1
if a != b:
    print("No adivinaste, mi número era ",a)
    
