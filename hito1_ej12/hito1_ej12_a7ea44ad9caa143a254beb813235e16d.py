#Juego adivina mi número
import random
n=int(random.randint(1,20))
aux=n
x=1
for n in range(5):
  nro=int(input("ingresa el numero a adivinar: "))
  if(nro==aux):
    print("Adivinaste, mi numero era",nro)
    break
  if(nro>aux):
    print("mi numero es menor ")
  if(nro<aux):
    print("mi numero es mayor ")
print("No adivinaste mi numero era",aux)