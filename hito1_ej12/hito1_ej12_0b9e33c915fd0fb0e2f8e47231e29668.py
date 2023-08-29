#Juego adivina mi número
import random
a=random.randint(1,20)
c=0
while c<5:
    b=int(input("Adivine el numero: "))
    if b==a:
        print("Adivino el numero =D")
        break
    if a<b:
        print("Su numero es mayor")
    elif a>b:
        print("Su numero es menor")
    c+=1
if c>=5:
    print("Mas suerte a la proxima")
    