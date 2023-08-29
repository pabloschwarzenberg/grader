#Ordenar tres números
A = eval(input("ingrese su primer numero: "))
B = eval(input("ingrese su segundo numero: "))
C = eval(input("ingrese su tercer numero: "))

Ma = max(A, B, C)
Mi = min(A, B, C)
H = (A + B + C) - Ma - Mi

print("Los numeros ordenados de menor a mayor son", Mi , "," ,H , "," ,Ma)