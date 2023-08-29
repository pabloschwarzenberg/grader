#Ordenar tres números
 # Definir la regla de ordenar los números de menor a mayor
def ordenar(a, b, c):
    numeros_ordenados = sorted([a, b, c])
    return ', '.join(str(num) for num in numeros_ordenados)

# Solicitar los tres números al usuario
num1 = int(input("Ingrese el 1.er número: "))
num2 = int(input("Ingrese el 2.do número: "))
num3 = int(input("Ingrese el 3.ro número: "))

#Mostrar resultado al usuario
resultado = ordenar(num1, num2, num3)
print("Números en orden:", resultado)     