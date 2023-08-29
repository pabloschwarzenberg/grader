#Juego adivina mi número
import random
num=random.randint(1,20)
n=1
while(n<=5):
  intento=int(input("ingrese numero: "))
  if(num==intento):
    print("adivinaste, mi numero era ",num)
    break
  elif(num<intento):
    print("mi número es menor")
  elif(num>intento):
    print("mi número es mayor")
  n=n+1
if(n>5):
  print("No adivinaste, mi número era ",num)