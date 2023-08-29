#Sistema de Ecuaciones
A = float(input("Ingrese a: "))
B = float(input("Ingrese b: "))
C = float(input("Ingrese c: "))
D = float(input("Ingrese d: "))
E = float(input("Ingrese e: "))
F = float(input("Ingrese f: "))
determint = A*E - B*D
X = (C*E - B*F) // determint
Y = (A*F - C*D) // determint

print("x = " + str(X) + "y = " + str(Y))