#Ordenar tres números

#El ingreso de números
num1 = int(input("Ingrese su número: "))
num2 = int(input("Ingrese su número: "))
num3 = int(input("Ingrese su número: "))

#Forma de ordenar los números
ordenNumeros = sorted([num1, num2, num3])

print("Números ordenados:", ", ".join(map(str, ordenNumeros)))