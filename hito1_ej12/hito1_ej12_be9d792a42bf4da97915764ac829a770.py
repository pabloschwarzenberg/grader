#Juego adivina mi número
import random

n=random.randint(1,20)
intento=1
while intento <=5:
	print("intento ", intento)
	num=int(input())
	if num==n:
		print("Adivinaste, mi número era ", n)
		break 
	elif intento==5:
		print("No adivinaste, mi número era ", n)
	intento+=1
