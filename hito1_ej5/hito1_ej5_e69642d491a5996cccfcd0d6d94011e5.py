#Cálculo del dígito verificador de un rut
# Solicitar el número de RUT al usuario
rut = input("Ingrese el número de RUT (sin guión ni dígito verificador): ")

# Validar que el RUT ingresado tenga al menos un dígito
if len(rut) > 0:
    # Invertir el RUT y convertirlo a una lista de dígitos
    rut_reverso = rut[::-1]
    digitos_rut = [int(d) for d in rut_reverso]

    # Calcular el dígito verificador
    factor = 2
    suma = sum([d * factor for d in digitos_rut])
    resto = suma % 11
    dv = 11 - resto

    # Verificar si el dígito verificador es 11 (0) o 10 (K)
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = "K"

    # Imprimir el dígito verificador
    print("dv =", dv)
else:
    print("El RUT ingresado es inválido.")
