#Ordenar tres números
A = int(input("ingrese un numero:"))
B = int(input("ingrese segundo numero:"))
C = int(input("ingrese tercer numero:"))
Ma = max(A,B,C)
Mi = min(A,B,C)
Me = (A + B + C) - Ma - Mi
print(Mi ," , ", Me ," , ",Ma)