#Juego adivina mi número
print("Intenta adivinar mi numero, esta entre el 1 y el 20")
a=int(input("En que numero estoy pensando :"))
import random
b = (random.randrange(20))
x = 1
while x < 5:
    if b > a:
        print("Mi numero es mayor")
        a=int(input("En que numero estoy pensando :"))
    elif b < a:
        print("Mi numero es menor")
        a=int(input("En que numero estoy pensando :"))
    elif a == b:
        print("Adivinaste, mi numero era",(b))
        break
    x = x + 1
print("No adivinaste, mi número era",(b))

        
      