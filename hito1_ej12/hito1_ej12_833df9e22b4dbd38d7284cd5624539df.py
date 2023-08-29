import random
n_secreto=random.randint(1,20)
jugador=int(input("Porfavor ingrese un numero"))
intentos=0
while intentos<4:
    if jugador!=n_secreto:
        if jugador<n_secreto:
            print("el numero ingresado es menor al numero real, intenta nuevamente")
            jugador=int(input("Porfavor ingrese un numero"))
            intentos+=1
        elif jugador>n_secreto:
            print("el numero ingresado es mayor al numero real, intenta nuevamente")
            jugador=int(input("Porfavor ingrese un numero"))
            intentos+=1
               
if jugador==n_secreto:
        print("Adivinaste, mi numero era", str( n_secreto))
       
else:
    print("No adivinaste, mi numero era",str(n_secreto))
    
