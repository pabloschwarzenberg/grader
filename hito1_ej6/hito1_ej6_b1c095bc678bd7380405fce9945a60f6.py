#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar los números de menor a mayor

    resultado = ",".join(str(num) for num in numeros)  # Convertir los números a cadenas y unirlos con comas

    return resultado

# Pedir al usuario que ingrese los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Llamar a la función y mostrar el resultado
resultado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados:", resultado)
      