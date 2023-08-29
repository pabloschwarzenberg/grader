import random
n = random.randint(1,20)
i=1
while i<=5:
    x= int(input("Adivina:"))
    if 0 < x <= 20:
        if x == n:
            print("Adivinaste, mi numero era: ", n)
            break
        else:
            if i == 5:
                print("No adivinaste, mi numero era:", n)
                break
            else:
                if x > n:
                    print("El número es menor")
                    i = i + 1
                else:
                    print("El número es mayor")
                    i = i + 1
    else:
        print("Tiene que ingresar un numero entre 1 y 20")