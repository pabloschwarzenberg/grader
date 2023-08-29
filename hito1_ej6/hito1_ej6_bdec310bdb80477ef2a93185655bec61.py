#Ordenar tres números
a = int(input("Ingrese número: "))
b = int(input("Ingrese número: "))
c = int(input("Ingrese número: "))
x = min(a,b,c)
z = max(a,b,c)
y = (a+b+c) - x - z
print("Los números ordenados son: {}, {}, {}".format(x,y,z))

