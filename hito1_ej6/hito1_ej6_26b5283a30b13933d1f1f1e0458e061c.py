#Ordenar tres números
X = int(input("ingresa un numero"))
Y = int(input("ingresa un segundo numero"))
Z = int(input("ingresa un tercer numero"))
Ma = max(X,Y,Z)
Mi = min(X,Y,Z)
Me = (X + Y + Z) - Ma - Mi
print(Mi ," , ", Me ," , ",Ma)