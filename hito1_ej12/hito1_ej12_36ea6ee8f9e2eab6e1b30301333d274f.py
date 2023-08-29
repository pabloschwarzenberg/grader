import random
#| JUEGO ADIVINA MI NUMERO |

number_of_intentos = 0



waa = random.randint (1, 20)



while number_of_intentos < 5:

    number_of_intentos = number_of_intentos + 1
    
    ELIGEELNUMERO= int(input("Elige un numerito, puedes elegir desde el 1 al 20: "))
    
    
    
    numerito_elegido = int(ELIGEELNUMERO)
    
    if numerito_elegido < waa:
    
    
        print("el numero es mayor")
        
    if numerito_elegido > waa:
    
    
        print("el numero es menor")
        
    if numerito_elegido == waa:
    
    
        break
    
if numerito_elegido == waa:


    print("¡Eres el mejor, Un master, un crack, un dios! lograste adivinar, el numero era", waa,)
if numerito_elegido != waa:


    print("JA! ¡Novato! No adivinaste, el numero era", waa,)  