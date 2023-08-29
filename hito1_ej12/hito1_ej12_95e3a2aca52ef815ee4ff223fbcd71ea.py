#Juego adivina mi número
import random
n_secreto=int(random.randint(1, 20))
cont=1
while(cont<=5):
  n_propuesto=int(input(""))
  if n_secreto==n_propuesto:
    print("Adivinaste! mi número era ",n_secreto)
    break
  elif n_secreto < n_propuesto:
    print("mi número es menor")
    cont += 1
  elif n_secreto > n_propuesto:
    print("mi número es mayor")
    cont += 1
  if cont == 6:
    print("No adivinaste, mi número era ", n_secreto)
  
    

    
   