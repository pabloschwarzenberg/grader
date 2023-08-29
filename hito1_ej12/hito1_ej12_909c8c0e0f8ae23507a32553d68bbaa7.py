#Juego adivina mi número
import random
a=random.randint(1,20)
b=0
print (a)
while b < 5:
      intento=int(input())
      if intento == a:
          print ("Adivinaste, mi numero era", (a))
      if intento > a:
          b=b+1
          print ("Mi numero es menor a eso")
      if intento < a:
          b=b+1
          print ("Mi numero es mayor a eso")
if b == 5:
    print ("No adivinaste, mi numero era", (a))
