#Ordenar tres números
A = int(input("Ingrese un numero:"))
B = int(input("Ingrese un segundo numero:"))
C = int(input("Ingrese un tercer numero:"))
Max = max(A,B,C)
Min = min(A,B,C)
Med = (A + B + C) - Max - Min
print(Min, ",",Med,",", Max)      