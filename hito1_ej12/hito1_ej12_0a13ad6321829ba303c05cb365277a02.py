from random import randint

posiblidad = randint(0,20)
intentos= 0

while intentos<5:
    print("adivina el numero tienes 5 intentos")
    adivina=input()
    adivina=int(adivina)
    
    intentos = intentos+1
    
    if adivina	< posiblidad:
        print("mi número es mayor")
        
    if adivina > posiblidad:
        print(" mi número es menor")
    
    if adivina==posiblidad:
        break
    
if adivina==posiblidad:
    intentos=str(intentos)
    print("adivinaste, mi numero era : ", posiblidad)
    
if adivina!=posiblidad:
    posiblidad=str(posiblidad)
    print("No adivinaste, mi numero era : ",posiblidad)
    