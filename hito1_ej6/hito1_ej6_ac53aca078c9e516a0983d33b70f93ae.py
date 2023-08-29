 #Ordenar tres números

A = int(input("Ingrese un numero:"))

B = int(input("Ingrese un segundo numero:"))

C = int(input("Ingrese un tercer numero:"))

Mayor = max(A,B,C)

Menor = min(A,B,C)

D = (A + B + C) - Mayor - Menor

print(Menor ," , ", D ,", ",Mayor)
     