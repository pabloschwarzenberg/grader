#Cálculo del dígito verificador de un rut
import math 

RUN =int(input("ingrese el run sin puntos ni guion:"))
A=(RUN//10000000)*3
B=((RUN//1000000)%10)*2
C=((RUN//100000)%10)*7
D=((RUN//10000)%10)*6
E=((RUN//1000)%10)*5
F=((RUN//100)%10)*4
G=((RUN//10)%10)*3
H=((RUN//1)%10)*2

SUMAR=(A+B+C+D+E+F+G+H)

RESTO=SUMAR//11
RESTO_=SUMAR -(11*RESTO)

RESTAR=11-RESTO_
if RESTAR == 11:
    print("dv=", end="")
    print(0)
elif RESTAR == 10:
    print("dv=", end="")
    print("k")
else:
    print("dv=",end="")
    print(RESTAR)
     