#Juego adivina mi número
import random

intentos=0
min_n=1
max_n=20
num=0
num_aleatorio=random.randint(1,20)
while intentos<5:
    if __name__ == "__main__":
        num=eval(input("Adivina el numero: "))
        num=int(num)
    intentos=intentos+1
    if num<num_aleatorio:
        print("Mi numero es mayor")
    elif num>num_aleatorio:
        print("Mi numero es menor")
if num==num_aleatorio:
    print("¡Adivinaste!, mi numero es",num_aleatorio) 
else:
    print("No adivinaste, mi numero era",num_aleatorio)
             