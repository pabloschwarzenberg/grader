#Cálculo del dígito verificador de un rut
## ENTRADA DE DATOS - PROCESO - SALIDA DE DATOS

Rut = input("Ingrese el RUT(sin puntos ni guión):")

if not Rut.isdigit()or len(Rut)< 7:
    print("RUT no válido. Debe ingresar solo números y debe ser al menos 7 digitos.")
else:
    Rut_reverso = Rut[::-1]
    multiplicador = 2
    Suma = 0

    for digito in Rut_reverso:
        Suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    Resto = Suma % 11
    dv = 11 - Resto
    if dv == 10:
        dv = "K"
    elif dv == 11:
        dv = 0

Rut_con_dv = Rut + "-" + str(dv)
print("dv =", dv)
     