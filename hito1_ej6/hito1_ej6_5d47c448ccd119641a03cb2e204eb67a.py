#Ordenar tres números
j = int(input("ingrese primer numero:"))
k = int(input("ingrese segundo numero:"))
l = int(input("ingrese tercer numero:"))

Menor = min(j , k , l)
Mayor = max(j , k , l)

resultado = (j + k + l) - Mayor - Menor

print("el orden de las variables de menor a mayor es: ", Menor, " , " , resultado, ", " , Mayor)