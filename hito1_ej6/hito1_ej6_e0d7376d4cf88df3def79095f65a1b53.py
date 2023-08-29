#Ordenar tres números
#Martín González B
n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
n3 = int(input("Ingrese tercer número: "))
a = min(n1, n2, n3)
c = max(n1, n2, n3)
b = (n1 + n2 + n3) - a - c
print("Los numeros ordenados son {}, {}, {}".format(a, b, c))