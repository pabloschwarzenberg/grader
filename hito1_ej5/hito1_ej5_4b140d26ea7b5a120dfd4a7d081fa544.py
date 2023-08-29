#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(7)  # Rellena con ceros a la izquierda si el Rut tiene menos de 7 dígitos

    factor = 2
    suma = 0

    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * factor
        factor = factor + 1 if factor < 7 else 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return "0"
    elif digito_verificador == 10:
        return "K"
    else:
        return str(digito_verificador)

rut = input("Ingrese el Rut sin dígito verificador: ")

digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)      