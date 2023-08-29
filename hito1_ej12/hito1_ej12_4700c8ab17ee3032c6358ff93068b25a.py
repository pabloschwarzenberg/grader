#Juego adivina mi número
from random import randint
num = int(input("Ingrese un número: "))
real = randint(1,20)
inte = 4

while num != real and inte > 0 :
 if num > real :
  print ("mi número es menor")
  inte = inte - 1


 if num < real :
  print ("mi número es mayor")
  inte = inte - 1

if inte == 0 and num != real :
 print("No adivinaste, mi número era: ",real)

else :
 print("Adivinaste, mi número era: ",real)
    
