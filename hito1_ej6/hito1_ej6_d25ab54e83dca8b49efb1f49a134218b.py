#Ordenar tres números
a = int(input("ingrese primer numero:"))
b = int(input("ingrese segundo numero:"))
c = int(input("ingrese tercer numero:"))

Menor = min(a , b , c)
Mayor = max(a , b , c)

total = (a + b + c) - Mayor - Menor

print("el orden de las variables de menor a mayor es: ", Menor, " , " , total, ", " , Mayor)