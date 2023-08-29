import random
a = (0)
numero = random.randint(1,20)
print("Hola !!!, estoy pensando un número del 1 al 20. Tienes 5 oportunidades para adivinarlo")
while a < 5:
    print("¿Cual es tu número?") 
    adivinar = input()
    adivinar = int(adivinar)
    if adivinar >= 1 and adivinar <= 20:
        a = a + 1
        if adivinar < numero:
            print(str(a) +". Muy bajo") 
        if adivinar > numero:
            print(str(a) +". Muy alto")
        if adivinar == numero:
            break
    else:
        print("Tu número esta fuera de rango. Intenta con otro número.")
       
if adivinar == numero:
    a = str(a)
    print("Adivinaste, mi numero era:",numero)
   
if adivinar != numero:
    numero = str(numero)
    print("No Adivinaste, mi numero era:" , numero)
