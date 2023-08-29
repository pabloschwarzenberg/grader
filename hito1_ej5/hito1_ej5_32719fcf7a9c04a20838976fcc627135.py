#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reverse_rut = rut_str[::-1]
    factors = [2, 3, 4, 5, 6, 7]
    sum_products = sum(int(reverse_rut[i]) * factors[i % 6] for i in range(len(reverse_rut)))
    dv = 11 - (sum_products % 11)
    
    if dv == 11:
        return "0"
    elif dv == 10:
        return "K"
    else:
        return str(dv)

# Solicitar al usuario ingresar el número de rut
rut = int(input("Ingrese un número de rut: "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Mostrar el resultado
print("dv=" + dv)