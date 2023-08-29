#Ordenar tres números
n1 = int(input("primer  numero: "))
n2 = int(input("segundo numero: "))
n3 = int(input("tercer  numero: "))

a = min(n1, n2, n3)
c = max(n1, n2, n3)
b = (n1 + n2 + n3) - a - c

print("los numeros ordenados son: ", (a, b, c))
