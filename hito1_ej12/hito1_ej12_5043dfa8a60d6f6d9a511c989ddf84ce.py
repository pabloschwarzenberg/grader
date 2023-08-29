import random
def generar_numero():
    global numero
    numero=random.randint(0,20)
    return numero

def adivina(n):
  i=0
  while i<=5:
    jugador=int(input())
    if jugador==n:
      print("Adivinaste, mi número era,",n)
    elif jugador<n:
      print("mi número es mayor")
      i+=1
    elif jugador>n:
      print("mi número es menor")
      i+=1
generar_numero()
adivina(numero)