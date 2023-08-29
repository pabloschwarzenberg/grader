import random as rnd
print("ADIVINA MI NÚMERO")
n = int(input("Ingrese un número entre 1 y 20: "))
a = rnd.randrange(1,20)
c = 1
while n != a and c < 5:
    if n > a:
        print("Mi número es menor")
        n = int(input("Ingrese un número entre 1 y 20: "))
    elif n < a:
        print("Mi número mayor")
        n = int(input("Ingrese un número entre 1 y 20: "))
    c = c + 1
if n == a:
        print("Adivinaste, mi número era:"+str(a))
else:
    print("No adivinaste, mi número era:" + str(a))