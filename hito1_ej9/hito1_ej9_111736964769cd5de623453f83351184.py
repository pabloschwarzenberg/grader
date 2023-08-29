#Sistema de Ecuaciones
x1 = int(input("primer valor"))
y1 = int(input("segundo valor"))
z1 = int(input("tercer valor"))
x2 = int(input("cuarto valor"))
y2 = int(input("quinto valor"))
z2 = int(input("sexto valor"))
determinante_s = (x1 * y2) - (x2 * y1)
determinante_x = (z1 * y2) - (z2 * y1)
determinante_y = (z2 * x1) - (z1 * x2)
x = determinante_x / determinante_s
y = determinante_y / determinante_s
print("x=",x)
print("y=",y)