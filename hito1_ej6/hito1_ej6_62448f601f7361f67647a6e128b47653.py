#Ordenar tres números
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese un segundo número entero: "))
n3 = int(input("Ingrese un tercer número entero: "))

Max = max(n1, n2, n3)
Min = min(n1, n2, n3)

X = (n1 + n2 + n3) - Max - Min

orden = print("De menor a mayor el orden es: ", Min," ,", X," ,", Max)