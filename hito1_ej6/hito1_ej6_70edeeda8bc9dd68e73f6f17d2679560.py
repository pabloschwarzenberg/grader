#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros_ordenados = sorted([a, b, c])
    numeros_cadena = [str(num) for num in numeros_ordenados]
    print(", ".join(numeros_cadena))

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

ordenar_numeros(num1, num2, num3)
