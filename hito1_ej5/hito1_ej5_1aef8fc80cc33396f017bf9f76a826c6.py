#Cálculo del dígito verificador de un rut
      def calcular_digito_verificador(rut):
    rut_invertido = str(rut)[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut_invertido:
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    resto = suma % 11
    digito_verificador = 11 - resto if resto != 0 else 0

    return digito_verificador

# Solicitar al usuario el RUT sin dígito verificador
rut_sin_dv = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut_sin_dv)

# Imprimir el resultado
print("dv =", digito_verificador)