import random

def ALTER():
    Num = random.randint(1,20)
    return Num

def numero(OP,Num):
    if OP > Num:
        print("Mi numero es menor")
    elif OP < Num:
        print("Mi numero es mayor")
    return

def Termin(OP,Num,cont):
    if OP == Num:
        print("Adivinaste, mi número era",Num)
        exit(-1)
    else:
        cont = cont - 1
        if cont == 0:
           print("No adivinaste, mi número era ",Num)
    return cont

cont = 5

while cont > 0:
    x = int(input("Ingrese número: "))
    cont = Termin(x, ALTER(), cont)
    if cont !=0: numOp = numero(x, ALTER())
