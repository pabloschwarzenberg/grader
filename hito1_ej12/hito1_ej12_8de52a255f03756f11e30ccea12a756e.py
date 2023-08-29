import random

y = random.randint(10,20)
m = 5
x = 1
n = int(input("ingresa un numero: "))

while (n != y) and (m>1):
    if(n>y):
        print("ingresa un numero menor")
    elif (n<y):
        print("ingresa un numero mayor")
    m = m - 1
    x = x + 1
    print("te quedan" , n , "intentos")
    n = int(input("ingresa un numero: "))
    
if (n == y):
    print("Adivinaste, mi numero era", y)
else:
    print("No adivinaste, mi numero y era", y)