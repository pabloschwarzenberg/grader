#Ordenar tres números
A= eval(input("Ingrese un numero: "))
B = eval(input("Ingrese un segundo numero: "))
C = eval(input("Ingrese un tercer numero: "))
Ma = max(A,B,C)
Mi = min(A,B,C)
Z = (A + B + C) - Ma - Mi
print("el orden de menor a mayor  es ", Mi ," , ", Z , " , ", Ma)  