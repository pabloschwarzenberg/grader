n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))

n_menor = min(n1, n2, n3)
n_mayor = max(n1, n2, n3)
n_medio = (n1 + n2 + n3) - n_menor - n_mayor

print(n_menor,",",n_medio,",",n_mayor)