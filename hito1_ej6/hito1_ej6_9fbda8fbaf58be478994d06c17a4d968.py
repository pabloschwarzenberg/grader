#Ordenar tres números
a = int(input("ingrese primer numero:"))
b = int(input("ingrese segundo numero:"))
c = int(input("ingrese tercer numero:"))

Menor = min(a , b , c)
Mayor = max(a , b , c)

resultado = (a + b + c) - Mayor - Menor

print("De menor a mayor el orden es: ", Menor, " , " , resultado, ", " , Mayor)