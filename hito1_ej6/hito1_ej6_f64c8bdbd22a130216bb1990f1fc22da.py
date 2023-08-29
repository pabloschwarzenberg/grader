n1 = int(input("Ingrese el Primer valor: "))
n2 = int(input("Ingrese el Segundo valor: "))
n3 = int(input("Ingrese el Tercer valor: "))

a = min(n1, n2, n3)
c = max(n1, n2, n3)
b = (n1 + n2 + n3) - a - c
print("Los numeros ordenados de menor a mayor son: {}, {}, {}".format(a, b, c))