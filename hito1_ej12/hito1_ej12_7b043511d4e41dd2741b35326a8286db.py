import random
num = random.randint(1,20)
i = 0
print(num)
while(i < 5):
    guess = int(input("Adivina: "))
    if(guess == num):
        print("Adivinaste, mi número era",num)
        break
    elif(guess > num):
        i += 1
        print("mi número es mayor")
    elif(guess < num):
        i += 1
        print("mi número es menor")
else:
    print("No adivinaste, mi número era",num)