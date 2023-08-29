#Ordenar tres números
A = eval(input("Ingrese su primer numero: "))
S = eval(input("Ingrese su segundo numero: "))
D = eval(input("Ingrese su tercer numero: "))

Ma = max(A,S,D)
Mi = min(A,S,D)

F = (A + S + D) - Ma - Mi
print("Los numeros ordenados de menor a mayor son ", Mi ," , ", F , ",", Ma)
    