import random 

for i in range(4):
     computador=int(random.randint(1,20))
     jugador=int(input("Escriba un numero entre el 1 y el 20"))
     
     if jugador<computador:
        print ("El numero ingresado es menor que el numero secreto")
        
     elif jugador>computador:
          print("El numero ingresado es mayor que el numero secreto")
      
     elif jugador==computador:
          print ("Adivinaste mi numero era", computador)
          
else:
    print ("No adivinaste, mi numero era", computador)