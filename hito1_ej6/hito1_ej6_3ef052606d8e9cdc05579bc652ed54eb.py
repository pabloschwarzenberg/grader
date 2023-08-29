#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    # Comparar los números para obtener el menor, el medio y el mayor
    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)
    medio = (num1 + num2 + num3) - menor - mayor

    # Imprimir los números ordenados
    print(menor, medio, mayor,sep=",")

# Solicitar al usuario ingresar los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Llamar a la función para ordenar y mostrar los números
ordenar_numeros(numero1, numero2, numero3)