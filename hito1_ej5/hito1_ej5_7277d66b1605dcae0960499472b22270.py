#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    suma = 0
    multiplicador = 2
    
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    verificador = 11 - (suma % 11)

    if verificador == 11:
        verificador = "0"
    elif verificador == 10:
        verificador = "k"

    return verificador
    
rut = input("Ingrese el RUT (sin puntos ni guión): ")

resultado = calcular_digito_verificador(rut)

print("dv=" + str(resultado))
