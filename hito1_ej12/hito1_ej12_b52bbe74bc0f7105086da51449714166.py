#Juego adivina mi número
import random
n=random.randint(1,20)
print(n)
i=0
while True:
    if i<5:
        numero=int(input())
        if numero==n:
            r="Adivinaste, mi número era "
            print(r,n)
            break
        elif numero<n:
            print("mi numero es mayor")
        elif numero>n:
            print("mi numero es menor")
    if i==5:
        print("No adivinaste, mi número era ",n)
        break
    i+=1
          