#Juego adivina mi número

import time
import random


def guest_num():
    random_number = random.randint(1,20)
    counter = 0
    my_num = int(input("Adivina mi numero "))
    while counter < 4:
        if my_num != random_number:
            if my_num < random_number:
                print("mi número es mayor")
            else:
                print("mi número es menor")
            my_num = int(input("Adivina mi numero "))
            counter = counter + 1
        else:
            print("Adivinaste, mi número era " + str(random_number))
            break

        if counter == 4:
            print("No adivinaste, mi número era " + str(random_number))
            break


guest_num()
      