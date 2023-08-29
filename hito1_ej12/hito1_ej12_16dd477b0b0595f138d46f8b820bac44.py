import random
print("====== ADIVINA EL NÚMERO ======")
computador = random.randint(1,20)
i=0
while i<5:
    i=i+1
    jugador=int(input("número: "))
    if (jugador < computador):
        print("Mi número es mayor")
    if (jugador > computador):
        print("Mi número es menor")  
    if jugador == computador:
        print("muy bien")
        break     
if computador == jugador:
    print("adivinaste, mi número era", computador)
if computador != jugador:
    print("No adivinaste, mi numero era",computador)
