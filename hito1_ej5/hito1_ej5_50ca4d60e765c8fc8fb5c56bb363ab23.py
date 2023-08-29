def calcular_digito_verificador(rut):
    rut_reversed = str(rut)[::-1] 
    factor = 2
    suma = 0

    for d in rut_reversed:
        suma += int(d) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return "k"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

rut = int(input("Ingrese el RUT (sin dígito verificador): "))

digito_verificador = calcular_digito_verificador(rut)

print("dv =", digito_verificador)


      