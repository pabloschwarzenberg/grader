#Ordenar tres números
x = int(input("Escriba el primero número:"))
y = int(input("Escriba el segundo número:"))
z = int(input("Escriba el tercer número:"))

#Minimo, máximo e intermedio
a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("De menor a mayor el órden es ", a ," , ", b , " , ", c)