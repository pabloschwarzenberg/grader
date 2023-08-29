#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a una cadena de caracteres
    rut = rut.zfill(8)  # Rellenar con ceros a la izquierda si es necesario
    
    multiplicador = 2
    suma = 0
    
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    
    resto = suma % 11
    dv = 11 - resto
    
    if dv == 10:
        dv = 'K'  # Si el dígito verificador es 10, se representa con la letra K
    elif dv == 11:
        dv = '0'  # Si el dígito verificador es 11, se representa con el dígito 0
    
    return dv
rut = input("Ingrese el número de RUT sin el dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + str(digito_verificador))