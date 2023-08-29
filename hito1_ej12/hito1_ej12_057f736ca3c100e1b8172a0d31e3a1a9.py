#Juego adivina mi número
import random 
x=(random.randrange(20))
for i in range(0,5):
   numero=int(input("ingrese un numero del 1 al 20"))
   if x ==numero:
      print("adivinaste el numero")
      break
   elif x<numero:
      print("no adivinaste el numero, es menor")
   elif x>numero:
      print("no adivinaste el numero, es mayor")
print("no adivinaste el numero, era:", x)