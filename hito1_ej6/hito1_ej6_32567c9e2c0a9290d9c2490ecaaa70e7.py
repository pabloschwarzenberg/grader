x = int(input("ingrese el primer número: "))
y = int(input("ingrese el segundo número: "))
z = int(input("ingrese el tercer número: "))
a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z)- a - c
print("Los números ordenados de menor a menor son:",(a, b, c))