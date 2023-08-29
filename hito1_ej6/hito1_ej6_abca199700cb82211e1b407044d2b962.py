A = eval(input("Ingrese su primer número: "))
B = eval(input("Ingrese su segundo número: "))
C = eval(input("Ingrese su tercer número: "))
Ma = max(A,B,C)
Mi = min(A,B,C)
D = (A + B + C) - Ma - Mi
print("Los números ordenados a menor a mayor es", Mi,",", D ,",", Ma)