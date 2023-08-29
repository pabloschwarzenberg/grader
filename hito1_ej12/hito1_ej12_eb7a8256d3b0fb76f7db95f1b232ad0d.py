#Juego adivina mi número
from random import randint

numero = randint(1,20)
intentos = 5
ganador = False
i = 1
while i <= 5:
  num = eval(input("intento {}: ".format(i)))
    if num =< numero:
    print("mi número es mayor")
    
    else num >= numero:
    print("mi número es menor")
    
 if num == numero:
    ganador = True
    break
    i += 1
  
if ganador:
  print("Adivinaste, mi número era".format(i))
 
else:
  print("No adivinaste, mi número era".format(i))    