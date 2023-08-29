#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin guión ni dígito verificador): ")

# Verificar si el RUT ingresado es válido
if not rut.isdigit() or len(rut) < 1:
    print("El número de RUT ingresado no es válido.")
else:
    # Calcular el dígito verificador
    rut = rut[::-1]  # Invertir el RUT
    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    # Imprimir el resultado
    print("dv =", digito_verificador)
     