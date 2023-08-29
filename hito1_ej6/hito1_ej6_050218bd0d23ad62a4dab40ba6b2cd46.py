# Ordenar 3 numeros de menor a mayor

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

# Proceso

if n1 > n2 and n1 > n3 and n2 > n3:
    print(n3, ",", n2, "," , n1)
if n1 > n2 and n1 > n3 and n3 > n2:
    print(n2, "," , n3, "," , n1)
if n2 > n1 and n2 > n3 and n1 > n3:
    print(n3, ", " , n1, "," , n2)
if n2 > n1 and n2 > n3 and n3 > n1:
    print(n1, "," , n3, "," , n2)
if n3 > n2 and n3 > 1 and n2 > n1:
    print(n1, "," , n2, "," , n3)
if n3 > n2 and n3 > 1 and n1 > n2:
    print(n2, "," , n1, "," , n3)
      