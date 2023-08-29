#Juego adivina mi número
import random
num_sec=random.randint(1,20)
contador=5
while contador>0:
 suerte=int(input("adivine pueh: "))
 if suerte==num_sec and contador>0:
  print("adivinaste, mi número era",num_sec)
  break
 elif suerte>num_sec:
  print("es mayor que el número secreto")
  contador=contador-1
 elif num_sec>suerte:
  print("es menor que el número secreto")
  contador=contador-1
 elif contador==0:
  break
  print("No adivinaste, mi número era",num_sec)
        
      