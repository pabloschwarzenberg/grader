#Juego adivina mi número
      
import random

x=random.randrange(21)
i= 21
l=5
while i != x and l > 0:
	i=int(input("Adivina el número: "))
	if(i>x):
		print("mi número es menor")
		l-=1
	elif(i<x):
		print("mi número es mayor")
		l-=1

if(l>0):
	print("Adivinaste, mi número era", x)
else:
	print("No adivinaste, mi número era", x)