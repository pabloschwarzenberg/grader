#Juego adivina mi número
      #Juego adivina mi numero
import random
numero= random.randint(1,20)
valor=0
intento = 1

while True:
    if intento < 6:
        valor = int(input("Adivina el numero: "))
        intento = intento + 1
        if valor != numero and intento<6:
            if valor < numero:
                print("El numero secreto es mayor, vuelve a intentar")
            else:
                print("El numero secreto es menor, vuelve a intentar")
            
        elif valor == numero:
            print("Adivinaste, mi numero era", numero)
            break
    elif intento == 6:
        print("No adivinaste, mi numero era",numero)
        break

    
    
    
