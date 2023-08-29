#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]  # Invertir el RUT
    factor = 2
    suma = 0
    
    # Calcular la suma ponderada
    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    # Calcular el dígito verificador
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return "K"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

# Solicitar el RUT al usuario
rut = input("Ingrese un número de RUT sin dígito verificador: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
     