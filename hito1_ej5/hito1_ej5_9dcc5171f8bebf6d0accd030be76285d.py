#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reversed = str(rut)[::-1]
    factor = 2
    suma = 0

    for digito in rut_reversed:
        suma += int(digito) * factor
        factor = factor + 1 if factor < 7 else 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return "dv=0"
    elif digito_verificador == 10:
        return "dv=K"
    else:
        return "dv=" + str(digito_verificador)


# Ejemplo de uso
rut = int(input("Ingrese el número de Rut sin dígito verificador: "))

resultado = calcular_digito_verificador(rut)
print(resultado)
      