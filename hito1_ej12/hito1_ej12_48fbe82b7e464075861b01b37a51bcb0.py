import random
noculto = random.randint(1,20)

cuenta = 5    
while cuenta > 0:
    numero=int(input("ingrese un numero: "))
    if cuenta == 0:
        break
    if numero > noculto:
        print("mi número es menor")
        cuenta = cuenta -1
    if numero < noculto:
        print("mi número es mayor")
        cuenta = cuenta -1
    if numero == noculto:
        print("Adivinaste, mi numero era", noculto)
        break
    if cuenta == 0:
        print("No adivinaste, mi número era ", noculto)
        break
