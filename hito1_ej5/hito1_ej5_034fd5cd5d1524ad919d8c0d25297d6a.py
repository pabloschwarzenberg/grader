def calcular_digito_verificador(rut):
    rut = str(rut).zfill(8)
    factor = 2
    suma = 0

    for i in range(7, -1, -1):
        suma += int(rut[i]) * factor
        factor += 1
        if factor == 8:
            factor = 2

    verificador = 11 - (suma % 11)
    if verificador == 10:
        return 'dv=K'
    elif verificador == 11:
        return 'dv=0'
    else:
        return 'dv=' + str(verificador)


rut_input = input("Ingrese el RUT (sin dígito verificador): ").strip()

if rut_input.isdigit():
    rut_input = int(rut_input)
    resultado = calcular_digito_verificador(rut_input)
    print(resultado)
else:
    print("El RUT ingresado no es válido.")