#ordene de menor a mayor
x = int(input("ingrese primer numero:"))
y = int(input("ingrese segundo numero:"))
z = int(input("ingrese tercer numero:"))
Menor = min(x, y, z)
Mayor = max(x, y, z)
Medio = x + y + z - Menor - Mayor
print("los numeros ordenados son:{}, {}, {}".format(Menor, Medio, Mayor))