#Sistema de Ecuaciones
A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())
y = (D*C - A*F)/(D*B - A*E)
Y = str(y)
x = (C - B*y)/A
X = str(x)
print("x="+X)
print("y="+Y)
