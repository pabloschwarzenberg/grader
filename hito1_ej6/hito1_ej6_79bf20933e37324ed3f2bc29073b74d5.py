#Ordenar tres números
X = int(input("Ingrese un numero:"))
Y = int(input("Ingrese el segundo numero:"))
Z = int(input("Ingrese el tercer numero:"))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
D = (X + Y + Z) - Ma - Mi
print(Mi, ",", D,",", Ma)