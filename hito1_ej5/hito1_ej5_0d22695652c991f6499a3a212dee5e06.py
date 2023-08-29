def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el orden del RUT
    multiplicador = 2
    suma = 0
    
    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        return "dv=0"
    elif digito_verificador == 10:
        return "dv=K"
    else:
        return "dv=" + str(digito_verificador)

# Ejemplo de uso:
rut = int(input("Ingresa el número de RUT sin dígito verificador: "))

digito_verificador = calcular_digito_verificador(rut)
print(digito_verificador)
