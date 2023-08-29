import random
n=random.randrange(20)

print("Adivina el numero de 1 a 20, tienes 5 intentos")
intentos=10
contador=0
lista=[n]
while (contador<intentos):
  numero=int(input("adivina : "))
  lista.append(numero)
  contador=contador+1

  if(n==numero):
    print("Adivinaste, mi número era",n)
    contador=6
    break
  elif(n>numero):
    print("mi número es mayor")
    contador=contador+1
  elif(n<numero):
    print("mi número es menor")
    contador=contador+1
  elif(intentos==contador):
    print("no adivinaste, mi número era",n)
    contador=6
    break

