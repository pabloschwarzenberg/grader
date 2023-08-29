def descomponer_numero(numero):
    # Descomponer el número en unidades, decenas, centenas y miles
    unidad = numero % 10
    decena = (numero // 10) % 10
    centena = (numero // 100) % 10
    mil = (numero // 1000) % 10
    
    # Retornar los numeros 
    return unidad, decena, centena, mil


# Solicitar al usuario un número de maximo 4 dígitos
numero_input = input("Ingrese un número de hasta 4 dígitos: ")
numero = int(numero_input)

# limitar el numero a 4 digitos
if numero < 0 or numero > 9999:
    print("El número ingresado está fuera del rango válido.")
else:
    #  descomposición del número
    unidad, decena, centena, mil = descomponer_numero(numero)
    
    # Construir la representación en texto de la descomposición
    representacion = ""
    if mil > 0:
        representacion += str(mil) + "M "
    if centena > 0:
        representacion += str(centena) + "C "
    if decena > 0:
        representacion += str(decena) + "D "
    if unidad > 0:
        representacion += str(unidad) + "U"
    
    # Imprimir el resultado
    print(representacion)
