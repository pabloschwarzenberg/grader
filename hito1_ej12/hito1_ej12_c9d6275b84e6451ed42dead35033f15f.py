import random
guessesTaken=0
minNumber=1
maxNumber=20


number=random.randint(1,20)

while guessesTaken<5:
    print("Cual es tu numero?: ")
    guess=input()
    guess=int(guess)
    guessesTaken=guessesTaken+1
    if guess<number:
        print("Mi numero es mayor")
    if guess>number:
        print("Mi numero es menor")
    if guess==number:
        break
if guess==number:
    guessesTaken=str(guessesTaken)
    number=str(number)
    print("Adivinaste, mi numero era" + number)
    
if guess!=number:
    number=str(number)
    print("No adivinaste, mi numero era"+ number)