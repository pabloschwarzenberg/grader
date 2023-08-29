#Descomponer un número
unidades = 0
decenas = 0
centenas = 0
miles = 0
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if numero > 9999 or numero < 0:
    print("El número ingresado está fuera del rango válido.") 
else:
    if numero > 0:
        miles = (numero // 1000) % 10
    if numero > 0:
        centenas = (numero // 100) % 10
    if numero > 0:
        decenas = (numero // 10) % 10
    if numero > 0:
        unidades = numero % 10
        

    print(f"la desconpocicion del numero {numero} es {miles}, {centenas}, {decenas}, {unidades}")    