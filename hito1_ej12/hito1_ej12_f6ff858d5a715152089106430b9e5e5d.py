#Juego adivina mi número

n_secreto = 13
n_jugador = 0
intentos = 5

while ((n_jugador != n_secreto) and (intentos > 0)):
    n_jugador = eval(input("Ingrese número: "))
    
    if (n_jugador > n_secreto):
        print("Mi número es menor")
        
    elif (n_jugador < n_secreto):
        print("Mi numero es mayor")
        
    intentos -= 1

if (n_jugador == n_secreto):
    print("Adivinaste, mi número era:", n_secreto)

else:
    if (intentos == 0):
        print("No adivinaste, mi número era:", n_secreto)