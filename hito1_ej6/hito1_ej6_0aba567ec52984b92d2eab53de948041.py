g = int(input("ingrese el primer numero: "))
d = int(input("ingrese el segundo numero: "))
s = int(input("ingrese el tercero numero: "))

a = min(g, d, s)
b = max(g, d, s)
c = (g + d + s) - a - b

print("los numeros ordenados de menor a mayor son: ", a,",", c,",", b)