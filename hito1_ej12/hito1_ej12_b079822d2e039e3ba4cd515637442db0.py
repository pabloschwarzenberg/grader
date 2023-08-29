#Juego adivina mi número
secreto = 15
num = 0
intento = 1

while(intento <= 5):
  num = eval(input("ingrese numero: "))
  intento = intento + 1
  if (intento > 5):
    print("No adivinaste, mi número era",secreto)
    break
  if (num < secreto):
    print("mi numero es mayor")
  elif (num > secreto):
    print("mi numero es menor")
  elif (num == secreto):
    print("Adivinaste, mi número era",secreto)
    break