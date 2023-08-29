#Ordenar tres números

A = eval(input("Ingrese su primer número: "))
B = eval(input("Ingrese su segundo número: "))
C = eval(input("Ingrese su tercer número: "))

Ma = max (A, B, C)
Mi = min (A, B, C)
D = (A + B + C) - Ma - Mi

print("Los numeros de menor a mayor son: ", Mi,",", D ,",", Ma)