import random
import sys
maquina=random.randint(1,20)
print(maquina)
jugador=int(input("ingresa un numero del 1 al 20 "))
if maquina>jugador:
  print("mi numero es mayor")
if maquina <jugador:
  print("mi numero es menor")
if maquina==jugador:
  sys.exit(print("Adivinaste, mi número era",maquina))
jugador2=int(input("intento 2 ingresa otro numero "))
if maquina>jugador2:
  print("mi numero es mayor")
if maquina <jugador2:
  print("mi numero es menor")
if maquina==jugador2:
  sys.exit(print("Adivinaste, mi número era",maquina))
jugador3=int(input("intento 3 ingresa otro numero "))
if maquina>jugador3:
  print("mi numero es mayor")
if maquina <jugador3:
  print("mi numero es menor")
if maquina==jugador3:
  sys.exit(print("Adivinaste, mi número era",maquina))
jugador4=int(input("intento 4 ingresa otro numero "))
if maquina>jugador4:
  print("mi numero es mayor")
if maquina <jugador4:
  print("mi numero es menor")
if maquina==jugador4:
  sys.exit(print("Adivinaste, mi número era",maquina))
jugador5=int(input("intento 5 ingresa otro numero "))
if maquina==jugador5:
  sys.exit(print("Adivinaste, mi número era",maquina))
if maquina !=jugador2:
  print("No adivinaste, mi número era",maquina)