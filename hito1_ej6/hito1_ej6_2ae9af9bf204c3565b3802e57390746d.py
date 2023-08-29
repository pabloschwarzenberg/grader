#Ordenar tres números
T = int(input("ingrese un numero:"))
Z = int(input("ingrese un segundo numero:"))
H = int(input("ingrese un tercer numero:"))
Ma = max(T,Z,H)
Mi = min(T,Z,H)
Me = (T + Z + H) - Ma - Mi
print(Mi ," , ", Me ,", ",Ma)