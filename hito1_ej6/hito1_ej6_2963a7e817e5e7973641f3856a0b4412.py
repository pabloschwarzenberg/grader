print("Por favor ingrese el numero que le plazca")
A = int(input("ingrese un numero :"))
B = int(input("ingrese un segundo numero :"))
C = int(input("ingrese un tercer numero :"))

Ma = max(A,B,C)
Mi = min(A,B,C)

S = (A + B + C) - Ma - Mi

print("El orden de menor a mayor es ",Mi,",",S,",",Ma)

