def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el número a una cadena de texto
    rut = rut.zfill(8)  # Rellenar con ceros a la izquierda si el RUT tiene menos de 8 dígitos

    factores = [3, 2, 7, 6, 5, 4, 3, 2]
    suma = sum(int(digito) * factor for digito, factor in zip(rut, factores))
    digito_verificador = 11 - (suma % 11)

    if digito_verificador == 11:
        dv = "0"
    elif digito_verificador == 10:
        dv = "K"
    else:
        dv = str(digito_verificador)

    return dv


# Ejemplo de uso
rut = input("Ingrese el número de RUT sin el dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)

   

    