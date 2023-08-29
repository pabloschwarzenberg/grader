#Sistema de Ecuaciones

print("ax+  by =c")
print("dx+  ey =f")
print("Introducir los valores de:")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = float(input("d ="))
e = float(input("e ="))
f = float(input("f ="))
# Procesos
x = (c*e-b*f)/(a*e-b*d)
y= (a*f-c*d)/(a*e-b*d)
# Exponder resultados
print("Los resultados son los siguentes")
print("X =",x)
print("Y =",y)