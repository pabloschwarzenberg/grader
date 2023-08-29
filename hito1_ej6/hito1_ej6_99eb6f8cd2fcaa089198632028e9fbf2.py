#Ordenar tres números
A = int(input("Primer valor: "))
B = int(input("Segundo valor= "))
C = int(input("Tercer valor= "))

X= min(A, B, C)
Y= max(A, B, C)
Z=(A + B + C) - X - Y

print("numeros ordenados de menor a mayor: {} , {} y {}". format(A, B, C))