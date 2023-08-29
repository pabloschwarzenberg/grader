#Ordenar tres números
X = eval(input("Ingrese el primer número: "))
Y = eval(input("Ingrese el segundo número: "))
Z = eval(input("Ingrese el tercer número: "))

Ma = max(X,Y,Z)
Mi = min(X,Y,Z)

Mid = (X + Y + Z) - Ma - Mi

print("Los números ordenados de menor a mayor son ", Mi, ",", Mid, ",", Ma)  