def calcular_digito_verificador(rut):
    rut = str(rut)
    # Eliminar puntos y guion del RUT, si los tiene
    rut = rut.replace(".", "").replace("-", "")
    
    # Validar que el RUT tenga al menos 1 dígito
    if len(rut) < 1:
        return "RUT inválido"
    
    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    # Obtener el dígito verificador
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return "dv=0"
    elif dv == 10:
        return "RUT inválido"
    else:
        return "dv=" + str(dv)


# Ingreso de datos
rut = input("Ingrese el número de RUT (sin puntos ni guión): ")

# Calcular el dígito verificador
resultado = calcular_digito_verificador(rut)

# Imprimir el resultado
print(resultado)