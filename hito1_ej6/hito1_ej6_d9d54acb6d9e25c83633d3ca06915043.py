A = int(input("Imgrese un numero:"))
B = int(input("Ingrese un segundo numero:"))
C = int(input("Imgrese um tercer numero:"))
Ma = max(A,B,C)
Mi = min(A,B,C)
D = (A + B + C) - Ma - Mi
print(Mi,",",D,",",Ma)