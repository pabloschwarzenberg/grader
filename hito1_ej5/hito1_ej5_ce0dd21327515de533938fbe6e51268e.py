#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el Rut a cadena de caracteres
    rut = rut[::-1]  # Invertir el Rut para facilitar los cálculos
    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 'dv=0'
    elif digito_verificador == 10:
        return 'dv=K'
    else:
        return 'dv=' + str(digito_verificador)

rut_input = input("Ingresa un Rut: ")
resultado = calcular_digito_verificador(rut_input)
print(resultado)
