#Ordenar tres números
A = eval(input("Ingresa primer numero: "))
B = eval(input("Ingresa segundo numero: "))
C = eval(input("Ingresa tercer numero: "))

MAX = max(A,B,C)

MIN = min(A,B,C)


D = (A + B + C) - MAX - MIN

print("De menor a mayor el órden es ", MIN ," , ", D , " , ", MAX)