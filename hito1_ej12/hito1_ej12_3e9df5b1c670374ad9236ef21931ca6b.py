import random
a=random.randint(1,20)
intento=0
while intento<5:
  n=int(input("Ingrese el numero: "))
  if(1<n<a and a<=20):
    print("Mi numero es mayor")
    intento = intento + 1
  elif(1<a<n and n<=20):
    print("Mi numero es menor")
    intento = intento + 1
  elif(n<1):
    print("Ese numero no esta dentro del rango ")
    intento = intento + 1
  elif(n>20):
    print("Ese numero no esta dentro del rango ")
    intento = intento + 1
  elif n == a:
    print("Adivinaste, mi numero era",a)

if intento == 5:
  print("No adivinaste, mi numero era",a)   