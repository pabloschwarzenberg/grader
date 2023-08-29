#Juego adivina mi número
import random 
j = randmo.randit(1,20)
i = 0
while (i < 5):
n = input("ingrese un numero:")
if (n < j): print ("Su numero es menor al numero secreto")
i = i +1
elif (n > j): print ("Su numero es mayor al numero secreto")
else: print ("Adivinaste, mi número era", n)
break
if (i == 5):
print ("No adivinaste, mi número era", n)