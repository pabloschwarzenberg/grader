#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    print("dv =", digito_verificador)



rut = int(input("Ingrese el RUT (sin guion ni dígito verificador): "))


calcular_digito_verificador(rut)