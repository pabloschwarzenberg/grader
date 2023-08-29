num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))
min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
num_medio = num1 + num2 + num3 - min_num - max_num
print(f"Los números ordenados de menor a mayor son: {min_num}, {num_medio}, {max_num}")