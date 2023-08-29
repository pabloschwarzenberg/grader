#Ordenar tres números
#ENTRADA

x = int(input("Escriba el primer número: "))
y = int(input("Escriba el segundo número: "))
z = int(input("Escriba el tercer número: "))

#PROCESO

a = min(x, y, z)
b = max(x, y, z)
c = (x + y+ z)- a - b

#SALIDA

print("Los números ordenados de menor a mayor son: {}, {}, {}".format(a, c, b))