#Descomponer un número
num= int(input("Ingrese un numero de hasta 4 digitos: "))

if num in range(100,999):
    unidad = num % 10
    num = num // 10
    decena = num % 10
    num = num // 10
    centena = num % 10
    num = num // 10
    print(str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U")
if num in range(1000,9999):
    unidad = num % 10
    num = num // 10
    decena = num % 10
    num = num // 10
    centena = num % 10
    num = num // 10
    mil = num % 10
    num = num // 10
    print(str(mil)+"M+"+str(centena) + "C+" + str(decena) + "D+" + str(unidad) + "U")
if num in range(10,99):
    unidad = num % 10
    num = num // 10
    decena = num % 10
    num = num // 10
    print(str(decena)+"D+"+str(unidad)+"U")
if num in range(0,9):
    unidad = num % 10
    num = num // 10
    print(str(unidad)+"U")