#Ordenar tres números
N = eval(input("Escoja su primer número: "))
M = eval(input("Escoja su segundo número: "))
L = eval(input("Escoja su tercer número: "))

Ma = max(N,M,L)
print("El número mayor es: ", Ma)
Mi = min(N,M,L)
print("El número menor es: ", Mi)

O = (N + M + L) - Ma - Mi

print("De menor a mayor el órden es: ", Mi ," , ", O , " , ", Ma)