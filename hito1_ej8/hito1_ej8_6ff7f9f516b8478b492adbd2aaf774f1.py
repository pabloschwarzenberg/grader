#Descomponer un número
num = int(input("Ingrese un número de hasta 4 dígitos: "))


if num > 9999 or num < 0:
    print("Número inválido. Debe tener hasta 4 dígitos y ser positivo.")
else:
    
    unidades = num % 10
    num = num // 10

    decenas = num % 10
    num = num // 10

    centenas = num % 10
    num = num // 10

    miles = num % 10

    
    print(str(miles) + "M + " + str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U")      