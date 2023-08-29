#Ordenar tres números
X = int(input("ingrese un numero:"))
Y = int(input("ingrese un segundo numero:"))
Z = int(input("ingrese un tercer numero:"))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
Me = (X + Y + Z) - Ma - Mi
print(Mi ,",", Me ,",",Ma)