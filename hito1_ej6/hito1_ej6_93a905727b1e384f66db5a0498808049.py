#Ordenar tres números
x = int(input("Ingrese el primer número: "))   
y = int(input("Ingrese el segundo número: "))    
z = int(input("Ingrese el tercer número: "))    

a = min (x, y, z)
c = max (x, y, z)
b = (x + y + z) - a - c

print("Los números ordenados de menor a mayor son: {}, {}, {}". format(a, b, c) )

