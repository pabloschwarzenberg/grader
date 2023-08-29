import random
numeroSecreto = random.randint(1,20)
i = 1
while i <= 5:
    numero = int(input("Intenta adivinar el número: "))
    i = i + 1
    if numero > numeroSecreto:
        print("mi número es menor")
  
    if numero < numeroSecreto:
        print("mi número es mayor")

    if numero == numeroSecreto:
        print("Adivinaste, mi número era: ",numeroSecreto)
        break
    if i == 5:
        print("No adivinaste, mi número era:  ",numeroSecreto)
        break