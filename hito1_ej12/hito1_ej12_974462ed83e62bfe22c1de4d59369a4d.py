import random
number = random.randint(1,20)
tries = 0

p = True

print(number)

while p:
    tries += 1

    if tries <= 5:
        guess = int(input("Adivina mi número: "))
        if guess == number:
            print("Adivinaste, mi número era", number)
            p = False
        elif guess < number:
            print("Mi número es mayor")
        elif guess > number:
            print("Mi numero es menor")
    else: 
        print("Has perdido, mi número era", number)
        p = False