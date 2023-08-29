#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        medio = num2
        mayor = num3
    else:
        medio = num3
        mayor = num2
elif num2 <= num1 and num2 < num3:
    menor = num2
    if num1 <= num3:
        medio = num1
        mayor = num3
    else:
        medio = num3
        mayor = num1
else:
    menor = num3
    if num1 <= num2:
        medio = num1
        mayor =num2
    else:
        medio = num2
        mayor = num1
dato = "%d, %d, %d" % (menor, medio, mayor)
print(dato)