#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número : "))
Menor = min(a , b, c)
Mayor = max(a , b, c)
resultado = (a + b + c) - Mayor - Menor
print("El orden de los números de menor a mayor es: ", Menor, " , " , resultado, ", " , Mayor)