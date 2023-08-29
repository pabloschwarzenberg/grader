#Sistema de Ecuaciones
A=float(input("Ingresar valor A:"))
B=float(input("Ingresar valor B:"))
C=float(input("Ingresar valor C:"))
D=float(input("Ingresar valor D:"))
E=float(input("Ingresar valor E:"))
F=float(input("Ingresar valor F:"))

if (A!=0 and (E*A!=-(D*B))):
    y = (F*A - D*C)/(E*A - D*B)
    x = (C - B*y)/A
    print("x=",round(x,1))
    print("y=",round(y,1))
    
elif (A==0 and D!=0) :
    y = C/B
    x = (F - E*C)/D*B
    print("x=",round(x,1))
    print("y=",round(y,1))


else :
    print("ERROR")