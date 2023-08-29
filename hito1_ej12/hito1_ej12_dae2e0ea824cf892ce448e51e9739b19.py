#Juego adivina mi númeroimport random
import random
print("Binvenido al juego ADIVINA MI NÚMERO")
print("Reglas: tendras 5 intentos y el juego solo puede dar 2 pistas: mi numero  es mayor o es menor")
print("comencemos")
ns=random.randrange(1,20)
int1=int(input("intento 1: "))
if(int1<ns):
    print(" número es mayor")
if(int1>ns):
    print(" número es menor")
if(int1==ns):
    print("Adivinaste, mi número era ",ns)
int2=int(input("intento 2: "))
if(int2<ns):
    print(" número es mayor")
if(int2>ns):
    print(" número es menor")
if(int2==ns):
    print("Adivinaste, mi número era ",ns)
int3=int(input("intento 3: "))
if(int3<ns):
    print(" número es mayor")
if(int3>ns):
    print("número es menor")
if(int3==ns):
    print("Adivinaste, mi número era ",ns)
int4=int(input("intento 4: "))
if(int4<ns):
    print(" número es mayor")
if(int4>ns):
    print(" número es menor")
if(int4==ns):
    print("Adivinaste, mi número era ",ns)
int5=int(input("intento 5: "))
if(int5<ns):
    print(" número es mayor")
if(int5>ns):
    print(" número es menor")
if(int5==ns):
    print("Adivinaste, mi número era ",ns)
else:
    print("No adivinaste, mi número era ",ns )