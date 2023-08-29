#Ordenar tres números
X = int(input("Ingrese el primer número: "))
Y = int(input("Ingrese el segundo número: "))
Z = int(input("Ingrese el tercer número: "))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
Me = (X + Y + Z) - Ma - Mi
print("Los números ingresados ordenados de menor a mayor son: ", Mi ," , ", Me ," , ", Ma)