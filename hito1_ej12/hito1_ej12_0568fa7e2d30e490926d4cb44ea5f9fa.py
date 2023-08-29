from random import randint

numero_para_adivinar = randint (1, 20)

intentos = 0
numero_adivinado = 0 

while intentos <= 5:
      if intentos > 1:
            numero_adivinado = int(input("intenta de nuevo: "))
      else:
            numero_adivinado = int(input("digita el numero que crees que tengo: "))
      intentos += 1
      if numero_adivinado == numero_para_adivinar:
            print("Adivinaste, mi número era", numero_para_adivinar )
            break
      if  numero_para_adivinar > numero_adivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", numero_para_adivinar )
            break