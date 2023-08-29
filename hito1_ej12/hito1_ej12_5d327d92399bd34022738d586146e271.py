#Juego adivina mi número
import random
i=0
while i<5:
  f=int(input("ingrese Numero: "))
  a=random.randint(1,20)
  if f>a:
    print("el numero es mayor")
  elif f<a:
    print("el numero es menor")
  else:
    print("Adivinaste el numero era",f)
    break
  i=i+1
print("Programa Terminado")