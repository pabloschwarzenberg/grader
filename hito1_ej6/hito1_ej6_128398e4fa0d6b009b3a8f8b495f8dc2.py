#Ordenar tres números
# Entradas

number_1 = int(input("Ingrese un primer numero: "))
number_2 = int(input("Ingrese un segundo numero: "))
number_3 = int(input("Ingrese un tercer numero: "))

# Ordenar numeros dados(condiciones)

if number_1 < number_2 < number_3:
    print(number_1, number_2, number_3, sep=", ")
elif number_3 < number_2 < number_1:
    print(number_3, number_2, number_1, sep=", ")
elif number_1 < number_3 < number_2:
    print(number_1, number_3, number_2, sep=", ")
elif number_3 < number_1 < number_2:
    print(number_3, number_1, number_2, sep=", ")
elif number_2 < number_1 < number_3:
    print(number_2, number_1, number_3, sep=", ")
elif number_2 < number_3 < number_1:
    print(number_2, number_3, number_1, sep=", ")
elif number_1 == number_2 < number_3:
    print(number_1, number_2, number_3, sep=", ")
elif number_3 < number_1 == number_2:
    print(number_3, number_1, number_2, sep=", ")
elif number_1 == number_3 < number_2:
    print(number_1, number_3, number_2, sep=", ")
elif number_2 < number_1 == number_3:
    print(number_2, number_1, number_3, sep=", ")
elif number_2 == number_3 < number_1:
    print(number_2, number_3, number_1, sep=", ")
elif number_1 < number_2 == number_3:
    print(number_1, number_2, number_3, sep=", ")
else:
    print("Los numeros ingresados son iguales.")      