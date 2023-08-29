#Juego adivina mi número
import random
numSecreto=random.randint(1,20)
acierto=0

for m in range(0,5):
    num=int(input("Ingrese número: "))
    if num>numSecreto:
        print("Mi número es menor, escoge otro")

    elif num<numSecreto:
        print("Mi número es mayor, escoge otro")

    else:
        acierto=1
        print("Adivinaste, mi número era: ",numSecreto)
        break
if acierto!=1:
    print("No adivinaste, mi número era: ",numSecreto)




