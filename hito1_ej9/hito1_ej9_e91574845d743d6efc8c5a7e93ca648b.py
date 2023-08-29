#Sistema de Ecuaciones
a1=float(input("Numero que acompaña a X1:"))
b1=float(input("Numero que acompaña a Y1:"))
c1=float(input("Numero libre en la ecuación 1:"))
a2=float(input("Numero que acompaña a X2:"))
b2=float(input("Numero que acompaña a Y2:"))
c2=float(input("Numero libre en la ecuación 2:"))
if (a2*b1-a1*b2==0):
    print("Las ecuaciones que conforman el sistema son inconsistentes, o poseen infinitas soluciones")

if (a2*b1-a1*b2!=0):
    print("X=" ,float((c2*b1-b2*c1)/(a2*b1-a1*b2)))
if (a1*b2-a2*b1!=0):
    print("Y=" ,float((c2*a1-a2*c1)/(a1*b2-a2*b1)))
