#Ordenar tres números
x = int(input("ingrese el primer numero entero: "))
y = int(input("ingrese el segundo numero entero: "))
z = int(input("ingrese el tercer numero entero: "))

a = min (x, y, z)
c = max (x, y, z)
b = (x + y + z) - a - c
print("los numeros ordenados son {} , {} , {}". format(a, b, c))