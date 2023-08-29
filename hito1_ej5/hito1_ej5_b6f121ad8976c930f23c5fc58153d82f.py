#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a una cadena de texto
    rut = rut[::-1]  # Invertir el RUT para empezar desde la derecha

    multiplicador = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

if __name__ == "__main__":
    rut = int(input("Ingrese el número de RUT (sin dígito verificador): "))

    digito_verificador = calcular_digito_verificador(rut)

    print("dv =", digito_verificador)
      