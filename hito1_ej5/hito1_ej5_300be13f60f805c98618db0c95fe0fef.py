def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el número a cadena
    rut = rut[::-1]  # Invertir el orden de los dígitos
    factor = 2
    suma = 0

    for d in rut:
        suma += int(d) * factor
        factor += 1
        if factor > 7:
            factor = 2

    verificador = 11 - (suma % 11)
    if verificador == 10:
        return 'k'
    elif verificador == 11:
        return '0'
    else:
        return str(verificador)

# Ejemplo de uso
rut = input("Ingrese el RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)
