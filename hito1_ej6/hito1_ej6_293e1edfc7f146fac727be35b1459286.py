#Ordenar tres números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

mayor_numero = 0
menor_numero = 0
numero_del_medio = 0

if num1 < num2 and num1 < num3:
    menor_numero = num1
    if num2 < num3:
        numero_del_medio = num2
        mayor_numero = num3
    else:
        numero_del_medio = num3
        mayor_numero = num2
elif num2 < num3:
    menor_numero = num2
    if num3 < num1:
        numero_del_medio = num3
        mayor_numero = num1
    else:
        numero_del_medio = num1
        mayor_numero = num3
else:
    menor_numero = num3
    if num2 < num1:
        numero_del_medio = num2
        mayor_numero = num1
    else:
        numero_del_medio = num1
        mayor_numero = num2

print(str(menor_numero) + ", " + str(numero_del_medio) + ", " + str(mayor_numero))