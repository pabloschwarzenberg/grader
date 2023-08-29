#Juego adivina mi número
import random 

def juego(a,aleatorio):
    i = 0
    ganador = False
    while i <= 5 and ganador == False:
        if a > 20:
            a = int(input("ingrese un nuevo numero (mayor que 20)"))
        elif a < 0:
            a = int(input("ingrese un nuevo numero (menor que 20)"))
        elif int(a) > 0 and int(a)<21: 
            if a == aleatorio:
                ganador = True
                return print("Adivinaste, mi número era {}".format(aleatorio))
            elif a != aleatorio:
                if a < aleatorio:
                    print("mi número es menor")
                    
                    i += 1
                else:
                    print("mi número es mayor")
                    i += 1
    if i == 5:
        return print("No adivinaste, mi número era {}".format(aleatorio))

juego(int(input("ingrese numero: ")), random.randint(1,20))
