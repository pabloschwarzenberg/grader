from random import randint
intentos=5


numero=randint(1,20)
print('Bueno, '', piensa un número entre 1 y 20.')

while intentos<5:
    print ('¡Adivínalo! Tienes 5 intentos')
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Demasiado pequeño!')

    if adivina>numero:
        print('¡Demasiado grande!')

    if adivina==numero:
        break
    adivina = adivina
if adivina==numero:
    intentos=str(intentos)
    print('Fabuloso, '', acertaste el número en '+intentos+' intentos. ¡Estarás orgulloso-a!')

if adivina!=numero:
    numero=str(numero)
    print('¡Qué fatalidad '' ! Yo estaba pensando en el número '+numero)