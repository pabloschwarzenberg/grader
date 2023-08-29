import random
i_r = 0
num = random.randint(1,20)
est = 0
while True:
    est = int(input("intenta adivinar!:"))
    i_r = i_r + 1
    if est < num:
        print("mi numero es mayor")
    if est > num:
        print("mi numero es menor")
    if est == num:
        break
    if i_r >4:
        break
if est == num:
    print("Adivinaste, mi número era:",num)
if est != num:
    print("No adivinaste, mi número era:",num)