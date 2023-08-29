#Juego adivina mi número
import random
cont = 0
nums = random.randrange(21)
while True:
    numj = int(input("Adivina mi número "))
    if numj == nums:
        print("Adivinaste, mi número era", nums)
        break
    elif numj < nums:
        print("Mi número es mayor")
        cont = cont + 1
        if cont == 5:
           print("No adivinaste, mi número era", nums)
           break
        else:
           continue
    elif numj > nums:
        print("Mi número es menor")
        cont = cont +1
        if cont == 5:
           print("No adivinaste, mi número era", nums)
           break
        else:
           continue