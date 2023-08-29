#Juego adivina mi número
import random

adivina = random.randrange(20)
intento = 0

while(intento < 5):
    print("Intento",intento + 1)
    num = int(input("Di un numero: "))
    if(num < adivina):
        print("mi número es mayor")
    elif(num > adivina):
        print("mi número es menor") 
    elif(num == adivina):
        print("Adivinaste, mi número era ",adivina)
        break
    intento = intento + 1

if(intento == 5):
    print("No adivinaste, mi número era ",adivina)