import random

intentos = 0

x = random.randint( 1, 20 )

print( "Hola , Bienvenido a mi primer juego...." )

while intentos < 5:
    intentos = intentos + 1
    print( "Elige un numero del 1 al 20" )
    numero = eval(input())
    numero = int( numero )
    if numero < x:
        print( "Mi numero es Mayor" )
    if numero > x:
        print( "Mi numero es Menor" )
    if numero == x:
        break
if numero == x:
    print( "Adivinaste, mi número era ",x )
if numero != x:
    print( "No adivinaste, mi número era ",x )