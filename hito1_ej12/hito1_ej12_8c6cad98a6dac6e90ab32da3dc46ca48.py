#Juego adivina mi número
 1 import random
2 
3 secret = random.randint(1, 20)
4 guess = 0
5 tries = 0
6 
7 print ("Mi nombre es Ding Ding, ¡tengo un número secreto!")
 8 print ("El número es del 1 al 30, ¡solo tienes 6 posibilidades!")
9 
10 while int(guess) != secret and tries < 5:
 11 print ("¿Cuál es el número que adivinaste?")
12 guess = input()
13 if int(guess) < secret:
 14 print ("¡El número es demasiado pequeño! ¡Adivina de nuevo!")
15 elif int(guess) > secret:
 16 print ("¡El número es demasiado grande! ¡Adivina de nuevo!")
17 tries = tries + 1
18 if int(guess) == secret:
 19 print ("¡Eres increíble! ¡Felicitaciones, lo has adivinado!")
20 else:
 21 print ("Has adivinado mal 6 veces, ¡juguemos de nuevo la próxima vez!")
 22 print ("Mi número secreto es:", secreto)

