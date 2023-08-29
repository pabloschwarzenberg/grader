numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if numero < 0 or numero > 9999:
    print("El número ingresado no pertenece al rango.")
else:
    unidades = (numero % 10)
    decenas = ((numero // 10) % 10)
    centenas = ((numero // 100) % 10)
    miles = (numero // 1000)

    print("{miles}M + {centenas}C + {decenas}D + {unidades}U:")

