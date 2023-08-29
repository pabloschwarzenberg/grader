#Juego adivina mi número
import random
numrandom = random.randint(1,20)
p=1
while p <= 5:
    w = int(input("Adivina mi numero: "))
    if w<numrandom:
        print("Mi numero es mayor")
    elif w>numrandom:
        print("Mi numero es menor")
    else:
      print("Adivinaste! y mi numero era", numrandom)
      break
    if p == 5:
        print("No adivinaste, mi nuevo era", numrandom)
    p+=1