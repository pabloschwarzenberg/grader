#Sistema de Ecuaciones
X1=float(input("X1= "))
Y1=float(input("Y1= "))
C1=float(input("C1= "))

X2=float(input("X2= "))
Y2=float(input("Y2= "))
C2=float(input("C2= "))

X=((C1*Y2-Y1*C2)/(X1*Y2-Y1*X2))
Y=((X1*C2-C1*X2)/(X1*Y2-Y1*X2))

print("x=",X)
print("y=",Y)