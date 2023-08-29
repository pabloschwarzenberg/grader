#Ordenar tres números
def Ordenar(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    Numordenados = ', '.join(str(num) for num in numeros)
    return Numordenados


N1 = int(input("Ingrese el primer número: "))
N2 = int(input("Ingrese el segundo número: "))
N3 = int(input("Ingrese el tercer número: "))

NORDENADO = Ordenar(N1, N2, N3)

print("Números ordenados de menor a mayor: ", NORDENADO)  