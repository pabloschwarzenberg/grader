def ord_num(n1, n2, n3):
    numeros = [n1, n2, n3]
    numeros.sort()
    numeros_str = ','.join(str(num) for num in numeros)
    return numeros_str

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

num_ord = ord_num(num1, num2, num3)
print("Números ordenados de mayor a menor:", num_ord)