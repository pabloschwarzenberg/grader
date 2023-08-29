#Cálculo del dígito verificador de un rut
# Función para calcular el dígito verificador de un RUT
def calcular_digito_verificador(rut):
    rut = str(rut)
    reverso = rut[::-1]
    multiplicador = 2
    suma = 0
    for digito in reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return '0'
    elif dv == 10:
        return 'K'
    else:
        return str(dv)

# Solicitar al usuario ingresar un número de RUT
rut = input("Ingresa el número de RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("El dígito verificador es:", digito_verificador)
  
