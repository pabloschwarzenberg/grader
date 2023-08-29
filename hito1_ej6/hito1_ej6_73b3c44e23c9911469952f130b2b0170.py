#Ordenar tres números
A = int(input("Introduzca su primer número: "))
B = int(input("Introduzca su segundo número: "))
C = int(input("Introduzca su tercer número: "))

Min = min(A,B,C)
Max = max(A,B,C)
Med = (A + B + C) - Max - Min

print("El orden de menor a mayor es: ", Min, ",", Med, ",", Max)