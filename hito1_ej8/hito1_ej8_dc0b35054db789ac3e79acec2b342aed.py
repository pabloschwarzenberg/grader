#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) == 1:
    unidades = numero[0]
    print(unidades + "U")
elif len(numero) == 2:
    decenas = numero[0]
    unidades = numero[1]
    print(decenas + "D + " + unidades + "U")
elif len(numero) == 3:
    centenas = numero[0]
    decenas = numero[1]
    unidades = numero[2]
    print(centenas + "C + " + decenas + "D + " + unidades + "U")
elif len(numero) == 4:
    miles = numero[0]
    centenas = numero[1]
    decenas = numero[2]
    unidades = numero[3]
    print(miles + "M + " + centenas + "C + " + decenas + "D + " + unidades + "U")
else:
    print("El número ingresado tiene más de 4 dígitos.")    