#Juego adivina mi número
import random
numero_secreto=random.randrange(1,20)
i=1
while i<5:
   intento=int(input("Intenta adivinar mi numero: "))
   if intento==numero_secreto:
      print("Adivinaste, mi número era",numero_secreto)
      break
   elif intento<numero_secreto:
      print("Has fallado, mi número es mayor")
      i=i+1
   elif intento>numero_secreto:
      print("Has fallado, mi número es menor")
      i=i+1
   if i==5:
      print("No adivinaste, mi número era",numero_secreto)