numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  
    
    numero = ', '.join(str(num) for num in numeros)
    
    return numero

numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
print("Su numero ordenado de menor a mayor es: , numeros_ordenados)
