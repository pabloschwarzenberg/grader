#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reverse_rut = rut_str[::-1]
    factors = [2, 3, 4, 5, 6, 7]
    total = sum(int(reverse_rut[i]) * factors[i % 6] for i in range(len(reverse_rut)))
    dv = 11 - (total % 11)
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = 'K'
    return dv

rut = int(input("Ingrese el número de RUT: "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
