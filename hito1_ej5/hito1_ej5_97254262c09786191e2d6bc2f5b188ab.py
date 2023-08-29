def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0
    
    # Calcular la suma ponderada de los dígitos del RUT
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    # Calcular el dígito verificador
    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'
    
    return digito_verificador

# Ejemplo de uso
rut = input("Ingrese el número del RUT (sin guiones ni dígito verificador): ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)