#Ordenar tres números
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
num3 = int(input("Ingrese un número: "))
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
medio = (num1 + num2 + num3)-( mayor + menor)
print(f"{menor},{medio},{mayor}")