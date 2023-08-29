import random
guessesTaken = 0
number = random.randint(1,20)
print("Estoy pensando un número del 1 al 20. Tienes 6 oportunidades para adivinarlo")
while guessesTaken < 6:
    print("Cual es tu numero") 
    guess = input()
    guess = int(guess)
    if guess >= 1 and guess <= 20:
        guessesTaken = guessesTaken + 1
        if guess < number:
            print(str(guessesTaken) +" Muy bajo")
        if guess > number:
            print(str(guessesTaken) +"Muy alto")
        if guess == number:
            break
    else:
        print("Tu numero esta fuera de rango. Intenta con otro número")
       
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Excelente !!! Adivinaste mi numero era "+guessesTaken+" oportunidades")

elif guess != number:
    number = str(number)
    print("No, El numero que estaba pensando es el ",number)
