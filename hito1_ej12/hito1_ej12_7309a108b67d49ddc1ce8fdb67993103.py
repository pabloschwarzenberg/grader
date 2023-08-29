from random import randint

Adivinar = randint (1, 20)

i = 0
n = 0 

while i <= 5:
      if i > 1:
            n = int(input("intenta de nuevo: "))
      else:
            n = int(input("¿que numero crees que tengo? "))
      i += 1
      if n == Adivinar:
            print("Adivinaste, mi numero era ", 
            Adivinar )
            break
      if  Adivinar > n:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if i == 5:
            print("No adivinaste, mi número era", Adivinar )
            break     