#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort() 
    numeros_str = [str(num) for num in numeros]  
    resultado = ", ".join(numeros_str)  
    return resultado

# Solicitar al usuario los tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función e imprimir el resultado
resultado = ordenar_numeros(num1, num2, num3)
print("Números ordenados:", resultado)
