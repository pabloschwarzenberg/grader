rut = input("Ingrese el número del RUT sin dígito verificador: ")

# Reversa el RUT y lo convierte en una lista de dígitos
rut_reversa = list(reversed(rut))

# Serie numérica para multiplicar los dígitos
serie = [2, 3, 4, 5, 6, 7]

# Variables de multiplicador y acumulador
multiplicador_index = 0
acumulador = 0

# Itera sobre los dígitos del RUT y realiza la suma ponderada
for digito in rut_reversa:
    acumulador += int(digito) * serie[multiplicador_index]
    multiplicador_index += 1
    if multiplicador_index == len(serie):
        multiplicador_index = 0

# Calcula el dígito verificador
resto = acumulador % 11
digito_verificador = ""

if resto == 0:
    digito_verificador = "0"
elif resto == 1:
    digito_verificador = "K"
else:
    digito_verificador = str(11 - resto)

print("dv =", digito_verificador)
