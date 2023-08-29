#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]  # Invierte el Rut para facilitar el cálculo
    factor = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    verificador = 11 - (suma % 11)
    if verificador == 11:
        dv = "0"
    elif verificador == 10:
        dv = "K"
    else:
        dv = str(verificador)

    return dv


# Ejemplo de uso
rut = input("Ingrese el Rut (sin dígito verificador): ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)
      