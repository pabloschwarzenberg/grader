from random import randint

num = randint(1, 21)
att, guess = 0, 0

while att < 5 or guess == num:
    guess = int(input())

    if guess > num:
        print("mi numero es menor")
    elif guess < num:
        print("mi numero es mayor")
    else:
        break

    att += 1

if guess == num:
    print("Adivinaste, mi número era", str(num))
else:
    print("No adivinaste, mi número era", str(num))