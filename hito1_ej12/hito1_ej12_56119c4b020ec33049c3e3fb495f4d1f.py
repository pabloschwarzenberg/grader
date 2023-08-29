import random
num = random.randint(1,20)
print(num)
intentos = 0
num_i = int(input("Ingrese un numero: "))

while intentos <= 5:
  
  if num_i == num:
    print("Adivinaste, mi número era",num)
    break

  elif intentos == 5:
    print("No adivinaste, mi número era",num)
    break

  elif num_i != num:
    intentos = intentos + 1
    if num_i > num:
      print("el número ingresado es menor que el número secreto")
    elif num_i < num:
      print("el número ingresado es mayor que el número secreto") 