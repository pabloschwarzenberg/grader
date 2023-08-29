import random
numeroSecreto=random.randint(1,20)
adivinaste=0
for i in range(0,5):
    numero=int(input("ingrese numero:"))
    if numero>numeroSecreto:
        print("mi numero es menor")
    elif numero<numeroSecreto:
        print("mi numero es mayor")
    else:
        adivinaste=1
        print("adivinaste, mi numero era",numeroSecreto)
        break
if adivinaste!=1:
        print("no adivinaste, mi numero era",numeroSecreto)  