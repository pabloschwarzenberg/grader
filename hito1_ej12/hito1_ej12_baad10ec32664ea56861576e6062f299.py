#Juego adivina mi número
import random
intentos = 1
num = random.randint (1, 20)

while intentos < 5:
    x = int(input("Adivina en que número estoy pensando:"))
    if num == x:
        print ("Adivinaste, mi número era", num)
    intentos = intentos + 1
    if x > num:
        print ("mi número es menor")
    if x < num:
        print ("mi número es mayor")
if x == num:
    print ("Adivinaste, mi número era", num)
if x != num:
    print("No adivinaste mi número era", num)