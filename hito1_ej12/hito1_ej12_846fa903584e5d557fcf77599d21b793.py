from random import*
numero = randint(1, 20) 
n = 0 
while n <= 5: 
  intento = int(input("ingrese numero aleatorio: "))
  if intento > numero:
    print("el numero secreto es menor") 
    n = n + 1
  elif  intento < numero: 
    print("el numero secreto es mayor")
    n = n + 1
  if intento == numero: 
    print("Adivinaste, mi numero era", numero)
    break 
  if n == 5: 
    print("No adivinaste, mi numero era", numero)
    break
