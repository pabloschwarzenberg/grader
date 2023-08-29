#Juego adivina mi número
import random
listaNumeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numeroSecreto=random.choice(listaNumeros)
intentos=5      
while intentos>0:
  intento=int(input("ingresa un numero"))
  if intento==numeroSecreto:
    print("Adivinaste, mi número era",numeroSecreto)
  elif numeroSecreto>intento:
    print("mi número es mayor")
    intentos-=1
  elif numeroSecreto<intento:
    print("mi número es menor")
    intentos-=1
if intentos==0:
  print("No adivinaste, mi número era",numeroSecreto)
  
  