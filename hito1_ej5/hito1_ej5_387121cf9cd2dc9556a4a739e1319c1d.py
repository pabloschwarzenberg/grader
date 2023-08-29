#Cálculo del dígito verificador de un rut
def calcular_digito_verif(rut):
    rut = str(rut).replace(".", "").replace("-", "")
    total, multiplicador = 0, 2

    for digito in reversed(rut):
        total += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    digito_verif = 11 - (total % 11)
    return str(digito_verif) if digito_verif < 10 else "k" if digito_verif == 10 else "0"

rut = input("Ingrese el RUT (sin puntos ni guión): ")
digito_verif = calcular_digito_verif(rut)
print("dv=" + digito_verif)
