numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if numero < 0 or numero > 9999:
    print("El número ingresado no es válido.")
else:
    unidades = numero % 10
    decenas = (numero % 100) // 10
    centenas = (numero % 1000) // 100
    miles = numero // 1000

    print("Descomposición del número:")
    print(miles, "M +", centenas, "C +", decenas, "D +", unidades, "U")





