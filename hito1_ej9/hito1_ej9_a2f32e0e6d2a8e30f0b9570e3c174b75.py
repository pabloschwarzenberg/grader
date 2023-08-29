#Sistema de Ecuaciones
A=(int(input("ingrese el numero de a: ")))
B=(int(input("ingrese el numero de b: ")))
C=(int(input("ingrese el numero de c: ")))
D=(int(input("ingrese el numero de d: ")))
E=(int(input("ingrese el numero de e: ")))
F=(int(input("ingrese el numero de f: ")))
fa=(A*E)-(B*D)
X=(C*E-B*F)/fa
Y=(A*F-C*D)/fa
round(X,1)
round(Y,1)
print("x=",X)
print("y=",Y)