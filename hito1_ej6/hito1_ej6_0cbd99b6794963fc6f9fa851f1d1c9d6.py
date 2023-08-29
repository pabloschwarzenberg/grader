#Ordenar tres números
a = int(input("Ingresar primer Número  "))
b = int(input("Ingresar segundo Número  "))
c = int(input("Ingresar tercer Número  "))

Z = min(a, b, c)
Y = max(a, b, c)
X = (a + b + c) -Z -Y

print("números enteros ordenados de menor a mayor son: {}, {}, {}".format(Z,X,Y))