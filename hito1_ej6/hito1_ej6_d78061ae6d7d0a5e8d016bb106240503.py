#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    numeros_str = [str(num) for num in numeros]  # Convertir los números a cadenas de texto
    resultado = ', '.join(numeros_str)  # Unir los números separados por comas
    print(resultado)

# Solicitar al usuario ingresar los tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)