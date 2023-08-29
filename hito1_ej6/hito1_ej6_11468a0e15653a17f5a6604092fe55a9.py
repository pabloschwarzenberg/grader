#ordene de menor a mayor
a = int(input("ingrese primer numero:"))
b = int(input("ingrese segundo numero:"))
c = int(input("ingrese tercer numero:"))
Menor = min(a, b, c)
Mayor = max(a, b, c)
Medio = a + b + c - Menor - Mayor
print("los numeros ordenados son:{}, {}, {}".format(Menor, Medio, Mayor))