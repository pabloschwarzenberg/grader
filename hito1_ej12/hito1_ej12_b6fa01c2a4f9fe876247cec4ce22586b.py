from random import randint

contador = 0
a = randint(1,20)

numero = int(input("ingrese el numero un numero del 1 al 20: "))

while numero != a:
  contador += 1
 
  if a > numero: 
    print("mi número es mayor")

  if a < numero:
    print("mi número es menor")

  if numero == a:
    print("Adivinaste, mi número era :", numero)

  if contador == 5:
    print("se acabo el numero de intentos")
    break

  numero = int(input("ingrese el numero un numero del 1 al 20: "))