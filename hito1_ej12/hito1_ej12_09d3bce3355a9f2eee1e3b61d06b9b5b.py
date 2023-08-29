#Juego adivina mi número
from random import randint
azar=randint(1,20)
uno=int(input("ingrese un número:"))
if (uno<azar):
    print("mi número es mayor")
    dos=int(input("ingrese otro número:"))
elif (uno>azar):
    print("mi número es menor")
    dos=int(input("ingrese otro número:"))
else:
    print("adivinaste, mi número era",uno)
if (dos<azar):
    print("mi número es mayor")
    tres=int(input("ingrese otro número:"))
elif (dos>azar):
    print("mi número es menor")
    tres=int(input("ingrese otro número:"))
else:
    print("adivinaste, mi número era",dos)
if (tres<azar):
    print("mi número es mayor")
    cuatro=int(input("ingrese otro número:"))
elif (tres>azar):
    print("mi número es menor")
    cuatro=int(input("ingrese otro número:"))
else:
    print("adivinaste, mi número era",tres)
if (cuatro<azar):
    print("mi número es mayor")
    cinco=int(input("ingrese otro número:"))
elif (cuatro>azar):
    print("mi número es menor")
    cinco=int(input("ingrese otro número:"))
if (cinco<azar):
    print("no adivinaste, mi número era",azar)
elif (cinco>azar):
    print("no adivinaste, mi número era", azar)
else:
    print("adivinaste, mi número era",azar)   