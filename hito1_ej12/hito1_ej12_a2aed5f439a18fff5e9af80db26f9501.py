#Juego adivina mi número
import random
numero_secreto=(random.randrange(21))

a=int(input())
intentos=4
while intentos>0:
 if a==numero_secreto:
     print("Adivinaste, mi número era",numero_secreto)
     break
 else:
      intentos=intentos-1
      if intentos==3:
        if numero_secreto>a:
          print("mayor")
        else:
          print("menor")
      b=int(input())
      if numero_secreto>b and intentos>0:
       print("mayor")
      else:
          if intentos>0:
            print("menor")
    
print("No adivinaste, mi número era",numero_secreto)
    
  