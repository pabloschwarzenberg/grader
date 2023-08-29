#Ordenar tres números
X = int(input("Ingresa un número: "))
Y = int(input("Ingresa un número: "))
Z = int(input("Ingresa un número: "))

Ma = max(X,Y,Z)
Mi = min(X,Y,Z)

D = (X+Y+Z) - Ma - Mi

print(Mi," , ", D , " , ", Ma)