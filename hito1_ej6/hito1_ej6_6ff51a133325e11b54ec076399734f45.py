# Ordenar tres números
num = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero entero: "))

if num < num2 and num3 > num2:
    print(f"{num},{num2},{num3}")
elif num2 > num and num2 > num3:
    print(f"{num3},{num},{num2}")
elif num3 > num and num > num2:
    print(f"{num2},{num},{num3}")
elif num > num3 and num2 > num3:
    print(f"{num3},{num2},{num}")
elif num > num3 and num3 > num2:
    print(f"{num2},{num3},{num}")
