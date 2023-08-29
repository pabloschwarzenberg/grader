#Descomponer un número
numero = input("Ingresa un número de hasta 4 dígitos: ")
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    numero = numero.zfill(4)

    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    print(miles,"M +",centenas,"C +",decenas,"D +",unidades,"U")
