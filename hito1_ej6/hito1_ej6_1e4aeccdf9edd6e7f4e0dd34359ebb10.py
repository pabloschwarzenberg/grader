x = int(input("ingrese un numero entero: "))
y = int(input("ingrese otro numero entero: "))
z = int(input("ingrese el ultimo numero entero: "))
a = min(x, y, z)
c = max (x, y, z)

b = (x+y+z)-a-c
print("los numeros ordenados de mayor a menor son:{}, {}, {}".format(a, b, c))