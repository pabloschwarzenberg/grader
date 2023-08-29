def ordenar_numeros (num1, num2, num3):
    numeros = [num1, num2, num3]
    num_ordenados = ", ".join(map(str, sorted(numeros)))
    return num_ordenados

num1 = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))
num3 = int(input("Ingresa el tercer numero entero: "))

num_ordenados = ordenar_numeros(num1, num2, num3)

print("Numeros ordenados de menor a mayor:", num_ordenados)
      