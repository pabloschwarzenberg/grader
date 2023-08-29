from os import system
system ("cls")
def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los números
    numeros = [num1, num2, num3]
    
    # Ordenar la lista de menor a mayor
    numeros.sort()
    
    # Imprimir los números separados por comas
    print(','.join(str(num) for num in numeros))

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

ordenar_numeros(num1, num2, num3)
 