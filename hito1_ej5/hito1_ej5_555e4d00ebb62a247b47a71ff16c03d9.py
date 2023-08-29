def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.replace(".", "")  # Eliminar los puntos del rut si los tiene
    rut = rut.replace("-", "")  # Eliminar el guion del rut si lo tiene
    
    # Calcular la suma del producto de cada dígito por la serie numérica
    serie = [2, 3, 4, 5, 6, 7]
    suma = 0
    serie_index = 0
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * serie[serie_index]
        serie_index = (serie_index + 1) % len(serie)
    
    # Calcular el resto de la división por 11
    resto = suma % 11
    
    # Calcular el dígito verificador
    if resto == 1:
        dv = "K"
    elif resto == 0:
        dv = "0"
    else:
        dv = str(11 - resto)
    
    return dv

# Ejemplo de uso
rut = input("Ingresa el RUT sin guion ni dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)