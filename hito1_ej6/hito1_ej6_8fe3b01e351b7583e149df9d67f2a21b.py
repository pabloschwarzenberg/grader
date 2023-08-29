#Ordenar tres números
X = int(input("ingrese su primer numero:"))
Y = int(input("ingrese su segundo numero:"))
Z = int(input("ingrese su tercer numero:"))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
D = (X + Y + Z) - Ma - Mi
print(Mi ," , ", D , " , ", Ma)
