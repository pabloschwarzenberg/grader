# Obtener el número del RUT sin el dígito verificador
rut_numero = input("Ingrese el número del RUT sin el dígito verificador: ")

# Convertir el número del RUT a una lista de dígitos en orden inverso
digitos_rut = list(rut_numero)[::-1]

# Definir la serie numérica para los multiplicadores
serie_numerica = [2, 3, 4, 5, 6, 7]

# Calcular la suma ponderada de los dígitos del RUT
suma_ponderada = sum(int(digito) * serie_numerica[i % len(serie_numerica)] for i, digito in enumerate(digitos_rut))

# Calcular el resto de la suma ponderada dividida por 11
resto = suma_ponderada % 11

# Calcular el dígito verificador
if resto == 0:
    digito_verificador = "0"
elif resto == 1:
    digito_verificador = "K"
else:
    digito_verificador = str(11 - resto)

# Imprimir el dígito verificador
print("dv=" + digito_verificador)
