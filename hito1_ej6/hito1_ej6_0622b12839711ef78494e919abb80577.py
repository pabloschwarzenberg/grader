num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 <= num2 and num1 <= num3:
    min = num1
    if num2 <= num3:
        mid = num2
        max = num3
    else:
        mid = num3
        max = num2
elif num2 <= num1 and num2 <= num3:
    min = num2
    if num1 <= num3:
        mid = num1
        max = num3
    else:
        mid = num3
        max = num1
else:
    min = num3
    if num1 <= num2:
        mid = num1
        max = num2
    else:
        mid = num2
        max = num1

print(min, ',', mid, ',', max) 