#Ordenar tres números
A = int(input("ingresa un numero porfavor:"))
B = int(input("ingresa un segundo numero porfavor:"))
C = int(input("ingresa un tercer numero porfavor:"))
maxi = max(A, B, C)
mini = min(A, B, C)
medi = (A + B + C) - maxi - mini
print(mini ,",", medi, ",", maxi, ", ahora estan en orden!" )