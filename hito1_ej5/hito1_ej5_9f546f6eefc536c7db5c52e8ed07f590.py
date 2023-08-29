#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    
    rut = str(rut)
    rut = rut.replace(".", "").replace("-", "")

    if not rut.isdigit() or len(rut) < 1:
        return "RUT inválido"

    suma = 0
    multiplicador = 2
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador


# Ejemplo de uso
rut = input("Ingrese un RUT sin dígito verificador: ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)      