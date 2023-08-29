def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir a cadena de texto
    
    # Calcular la suma del producto de cada dígito por la serie numérica
    multiplicador = 2
    suma = 0
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    
    # Calcular el dígito verificador
    resto = suma % 11
    dv = 11 - resto
    
    # Asignar el dígito verificador según las reglas
    if dv == 11:
        dv = "0"
    elif dv == 10:
        dv = "K"
    
    return dv

# Pedir al usuario que ingrese el RUT
rut_input = input("Ingrese el número del RUT: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut_input)

# Imprimir el resultado
print("dv=",digito_verificador)