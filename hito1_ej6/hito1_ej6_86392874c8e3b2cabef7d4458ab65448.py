#Ordenar tres números de menor a  mayor#

X = int(input("Ingrese el primer número: "))
Y = int(input("Ingrese el segundo número: "))
Z = int(input("Ingrese el tercer número: "))

Mi = min(X, Y, Z)
Ma = max(X, Y, Z)
D = (X + Y + Z) - Ma - Mi

print(Mi ," , ", D ,", ",Ma)
