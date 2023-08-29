X = int(input("Ingrese un numero:"))
Y = int(input("Ingrese un segundo numero:"))
Z = int(input("Ingrese un tercer numero:"))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
Me = (X + Y + Z) - Ma - Mi
print(Mi ," , ", Me ,", ",Ma)