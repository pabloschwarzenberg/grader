#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT: ")

if not rut.isdigit() or len(rut) < 1:
    print("Error: El RUT ingresado no es válido.")
else:
    rut = rut[::-1]
    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = 0
        
    print("dv =", digito_verificador)      