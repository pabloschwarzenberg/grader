#Ordenar tres números
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un segundo numero: "))
n3 = int(input("Ingrese un tercer numero: "))

a = min(n1, n2, n3)
c = max(n2, n2, n3)
b = (n1 + n2 + n3) - a - c

print("El orden de los numeros es", a, "," , b, "," , c)      